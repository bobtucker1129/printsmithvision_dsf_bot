import streamlit as st
from db.db_conn import get_connection

st.title("PrintSmithVision DSF Bot")

invoice_number = st.text_input("Enter Invoice Number (6 digits)")

if invoice_number and invoice_number.isdigit() and len(invoice_number) == 6:
    st.success(f"Looking up Invoice #{invoice_number}...")

    conn = get_connection()
    cur = conn.cursor()

    try:
        # --- Fetch invoice data ---
        cur.execute("""
            SELECT 
                invoicenumber, takenby, proofreader, wanteddate, account_id, customerpo, weborderexternalid
            FROM invoicebase
            WHERE invoicenumber = %s
        """, (invoice_number,))
        row = cur.fetchone()

        if row:
            st.subheader("Invoice Summary")
            columns = [desc.name for desc in cur.description]
            for label, value in zip(columns, row):
                st.write(f"**{label}**: {value}")

            # --- Assign Project Manager (Taken By) ---
            st.subheader("Assign Project Manager")
            pm_list = ["Melissa", "Jim", "Steve", "Abi", "Ellie", "Shelley"]
            selected_pm = st.selectbox("Choose PM to assign:", pm_list)

            if st.button("Assign Taken By"):
                update_cur = conn.cursor()
                update_cur.execute("""
                    UPDATE invoicebase
                    SET takenby = %s
                    WHERE invoicenumber = %s
                """, (selected_pm, invoice_number))
                conn.commit()
                update_cur.close()
                st.success(f"✅ Taken By set to {selected_pm}")
            # --- Set Proofreader to DSF ---
            st.subheader("Proofreader")
            if st.button("Set Proofreader to DSF"):
                try:
                    proof_cur = conn.cursor()
                    proof_cur.execute("""
                        UPDATE invoicebase
                        SET proofreader = 'DSF'
                        WHERE invoicenumber = %s
                    """, (invoice_number,))
                    conn.commit()
                    proof_cur.close()
                    st.success("✅ Proofreader set to DSF")
                except Exception as e:
                    st.error(f"Update failed: {e}")
            # --- Set Jobbase Location Based on Press/Copier/Method ---
            st.subheader("Assign Job Locations with AI Logic")

            if st.button("Auto-Assign Locations"):
                try:
                    # Step 1: Mappings
                    machine_location_map = {
                        "B&W Digital Press": 2726,
                        "Digital Color Press": 2723,
                        "Xerox Baltoro": 18697147,
                        "FireJet": 24053172
                    }

                    pricing_method_location_map = {
                        "Fulfillment": 22439945,
                        "Multi-part Job": 2733,
                        "Mail Services": 2713,
                        "Outsource": 21116818,
                        "Digital Envelope Press": 2731
                    }

                    def determine_location(press, copier, method):
                        if press and press in machine_location_map:
                            return machine_location_map[press]
                        elif copier and copier in machine_location_map:
                            return machine_location_map[copier]
                        elif method and method in pricing_method_location_map:
                            return pricing_method_location_map[method]
                        return None

                    job_cur = conn.cursor()
                    job_cur.execute("""
                        SELECT
                            jobbase.id,
                            pressdefinition.name AS press_name,
                            copierdefinition.machinename AS copier_name,
                            ppm.abbreviation AS pricing_method
                        FROM jobbase
                        LEFT JOIN pressdefinition ON jobbase.pricingpress_id = pressdefinition.id
                        LEFT JOIN copierdefinition ON jobbase.pricingcopier_id = copierdefinition.id
                        LEFT JOIN preferencespricingmethod ppm ON jobbase.pricingmethod_id = ppm.id
                        WHERE jobbase.parentinvoice_id = (
                            SELECT id FROM invoicebase WHERE invoicenumber = %s
                        )
                    """, (invoice_number,))
                    jobs = job_cur.fetchall()

                    update_cur = conn.cursor()
                    updated_count = 0

                    for job_id, press_name, copier_name, pricing_method in jobs:
                        loc_id = determine_location(
                            press_name, copier_name, pricing_method)
                        if loc_id:
                            update_cur.execute(
                                "UPDATE jobbase SET location_id = %s WHERE id = %s",
                                (loc_id, job_id)
                            )
                            updated_count += 1

                    conn.commit()
                    update_cur.close()
                    job_cur.close()

                    st.success(
                        f"✅ Updated {updated_count} job parts with new location_id values")

                except Exception as e:
                    st.error(f"Location logic update failed: {e}")

        else:
            st.warning("No invoice found with that ID.")

    except Exception as e:
        st.error(f"Query failed: {e}")

    finally:
        cur.close()
        conn.close()
else:
    st.info("Please enter a valid 6-digit invoice number.")

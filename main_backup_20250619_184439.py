import streamlit as st
import re
from db.db_conn import get_connection

st.title("PrintSmithVision DSF Bot")

invoice_number = st.text_input("Enter Invoice Number (6 digits)")

show_stock_section = st.checkbox("Show Stock Order Section")

if invoice_number and invoice_number.isdigit() and len(invoice_number) == 6:
    st.success(f"Looking up Invoice #{invoice_number}...")
    conn = get_connection()
    cur = conn.cursor()

    try:
        # --- Fetch invoice data ---
        cur.execute("""
            SELECT 
                invoicenumber, takenby, proofreader, wanteddate, account_id, customerpo, weborderexternalid,
                (SELECT title FROM account WHERE id = invoicebase.account_id) AS customername
            FROM invoicebase
            WHERE invoicenumber = %s
        """, (invoice_number,))
        row = cur.fetchone()

        if row:
            st.subheader("Invoice Summary")
            columns = [desc.name for desc in cur.description]
            for label, value in zip(columns, row):
                st.write(f"**{label}**: {value}")

            customername = row[-1]  # from subquery result

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
                                "UPDATE jobbase SET location_id = %s WHERE id = %s", (loc_id, job_id))
                            updated_count += 1

                    conn.commit()
                    update_cur.close()
                    job_cur.close()

                    st.success(
                        f"✅ Updated {updated_count} job parts with new location_id values")
                except Exception as e:
                    st.error(f"Location logic update failed: {e}")

            # --- AI-Assisted Description Cleanup ---
            st.subheader("Clean Job Descriptions")

            if st.button("Clean Up Descriptions"):
                try:
                    def clean_description(desc):
                        if not desc:
                            return desc
                        for sep in [" - ", " – ", " — "]:
                            parts = desc.split(sep)
                            if len(parts) == 2 and parts[0].strip().lower() == parts[1].strip().lower():
                                return parts[0].strip()
                        return desc.strip()

                    fetch_cur = conn.cursor()
                    fetch_cur.execute("""
                        SELECT id, description
                        FROM jobbase
                        WHERE parentinvoice_id = (
                            SELECT id FROM invoicebase WHERE invoicenumber = %s
                        )
                    """, (invoice_number,))
                    jobs = fetch_cur.fetchall()

                    update_cur = conn.cursor()
                    updated = 0

                    for job_id, desc in jobs:
                        cleaned = clean_description(desc)
                        if cleaned != desc and cleaned != "":
                            update_cur.execute(
                                "UPDATE jobbase SET description = %s WHERE id = %s", (cleaned, job_id))
                            updated += 1

                    conn.commit()
                    fetch_cur.close()
                    update_cur.close()

                    st.success(f"✅ Cleaned {updated} job descriptions")
                except Exception as e:
                    st.error(f"Description cleanup failed: {e}")

            # --- Generate Invoice Title from Job Codes ---
            st.subheader("Generate Invoice Title")

            if st.button("Generate Invoice Title from Job Codes"):
                try:
                    cur.execute("""
                        SELECT jobbase.description
                        FROM jobbase
                        INNER JOIN invoicebase ON jobbase.parentinvoice_id = invoicebase.id
                        WHERE invoicebase.invoicenumber = %s
                    """, (invoice_number,))
                    descs = cur.fetchall()
                    codes = set()

                    def extract_code(desc):
                        if not desc:
                            return None
                        clean = re.split(r"\s*[-–—]\s*", desc)[0].strip()
                        match = re.match(
                            r"^([A-Z]{2,5}\d{2,5}[A-Z]?)(?:[_\s\-]|$)", clean)
                        return match.group(1) if match else clean

                    for row in descs:
                        code = extract_code(row[0])
                        if code:
                            codes.add(code)

                    if len(codes) > 1:
                        code_str = ", ".join(sorted(codes))
                        cur.execute("""
                            UPDATE invoicebase SET name = %s
                            WHERE invoicenumber = %s
                        """, (code_str, invoice_number))
                        conn.commit()
                        st.success(f"✅ Invoice title updated to: {code_str}")
                    else:
                        st.info("ℹ️ Only one job part found, no update needed.")

                except Exception as e:
                    st.error(f"Title generation failed: {e}")

            # --- Optional: Order Stock ---
            if show_stock_section:
                st.subheader("Order Stock")
                if st.button("Place Stock Order for All Parts"):
                    try:
                        stock_cur = conn.cursor()
                        stock_cur.execute("""
                            SELECT 
                                jobbase.id AS job_id,
                                jobbase.jobindex AS job_number,
                                invoicebase.invoicenumber,
                                stockdefinition.name AS stock_name,
                                stockdefinition.vendor_id,
                                stockdefinition.weight
                            FROM jobbase
                            INNER JOIN invoicebase ON jobbase.parentinvoice_id = invoicebase.id
                            INNER JOIN stockdefinition ON jobbase.stock_id = stockdefinition.id
                            WHERE invoicebase.invoicenumber = %s
                        """, (invoice_number,))
                        stock_jobs = stock_cur.fetchall()

                        if not stock_jobs:
                            st.info("ℹ️ No job parts with stock assigned.")
                        else:
                            insert_cur = conn.cursor()
                            inserted = 0

                            for row in stock_jobs:
                                job_id, job_number, inv_num, stock_name, vendor_id, weight = row
                                sheet_size = None

                                insert_cur.execute(
                                    "SELECT nextval('modelbase_id_seq')")
                                new_id = insert_cur.fetchone()[0]
                                insert_cur.execute(
                                    "INSERT INTO modelbase (id, isdeleted) VALUES (%s, false)", (new_id,))

                                insert_cur.execute("""
                                    INSERT INTO stockorder (
                                        id, customername, filled, invoicenumber, jobnumber, name,
                                        orderquantity, placed, receivedquantity, sheetsize, totalcost,
                                        vendorstocknumber, weight, vendor_id, color_id, enterdate,
                                        rollwidth, stockunit, extraqty, rollweight, isdeleted
                                    ) VALUES (
                                        %s, %s, false, %s, %s, %s,
                                        500, NULL, NULL, %s, 0,
                                        NULL, %s, %s, NULL, NOW(),
                                        NULL, 1, NULL, 0, false
                                    )
                                """, (new_id, customername, inv_num, job_number, stock_name,
                                      sheet_size, weight, vendor_id))
                                inserted += 1

                            conn.commit()
                            insert_cur.close()
                            st.success(
                                f"✅ Stock order(s) placed for {inserted} job part(s).")

                        stock_cur.close()
                    except Exception as e:
                        st.error(f"Stock order insert failed: {e}")

        else:
            st.warning("No invoice found with that ID.")

    except Exception as e:
        st.error(f"Query failed: {e}")

    finally:
        cur.close()
        conn.close()

else:
    st.info("Please enter a valid 6-digit invoice number.")

Stock Order Quantity - Implementation Notes

Context
In the PrintSmithVision_DSF_Bot, part of our automation involves inserting stock orders for jobs with assigned stock. One of the required fields is orderquantity, which determines how much stock is ordered for a given job part.

Issue
During analysis of the PrintSmith schema and observed system behavior:

The orderquantity value is not stored directly in stockdefinition, jobbase, or any immediately related table.

The GUI for PrintSmith typically allows users to manually enter this value when placing a stock order.

When the "Order Stock" button is pressed via the PrintSmith interface, the system sometimes defaults this value to 0 until it is manually overridden.

Investigated Sources

stockdefinition: Does not contain orderquantity. Most relevant fields are vendor_id, weight, and name (where vendor stock number is embedded).

jobbase: Contains sheet count and production metrics, but no direct stock quantity field.

GUI behavior: Often results in orderquantity = 0 until human intervention.

Current Approach
To maintain functionality and simulate GUI behavior:

We are currently defaulting orderquantity = 500 as a placeholder.

This number is conservative and based on common small-run jobs.

It can be manually overridden later in PrintSmith if needed.

Future Enhancements (Optional)
We may later implement logic that estimates a more accurate orderquantity using the following:

sheets from jobbase

numup from jobbase

pressqty, binderywaste, estwaste (job-level waste calculations)

Additional quantity logic from estimates or sales order entries (if accessible)

Why This Matters
Using a static default helps ensure jobs don't get overlooked in the stock order process, while keeping the process safe and editable. This also mirrors PrintSmith behavior where jobs often appear in the stock report with zero or default quantity until confirmed.

Summary

orderquantity is not determinable directly from the DB

Defaulted to 500 in our insert for now

Future logic may refine this

This README documents the current rationale for the team and future devs

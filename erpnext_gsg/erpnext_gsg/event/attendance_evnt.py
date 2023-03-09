import frappe
from frappe.utils import time_diff_in_hours

@frappe.whitelist()
def clac_hours(doc, event):
    if doc.check_out and doc.check_in:
        doc.hours = time_diff_in_hours(doc.check_out, doc.check_in)
    else:
        doc.hours = 0
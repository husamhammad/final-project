import frappe
from frappe.model.naming import make_autoname

# Check The naming series field and set new value in 
def payment_entry_before_insert(doc, method):
    if not doc.naming_series or doc.naming_series:
        doc.naming_series = 'GSG-JV-.YYYY.-'

    doc.name = make_autoname(doc.naming_series + '#####')

#  Set and Savd New Value For Naming Series In DataBase

def payment_entry_on_update(doc, method):
    frappe.db.set_value('Payment Entry', doc.name, 'naming_series', doc.naming_series)
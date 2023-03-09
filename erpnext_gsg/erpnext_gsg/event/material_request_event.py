import frappe
@frappe.whitelist()
def create_stock_entry(doc, event):
    print(doc.items[0].item_code)    
    if(doc.material_request_type != "Material Issue"):
        return
        
    from erpnext.stock.doctype.material_request.material_request import make_stock_entry
    new_stock_entry = make_stock_entry(doc.name)
    new_stock_entry.insert()
    new_stock_entry.submit()
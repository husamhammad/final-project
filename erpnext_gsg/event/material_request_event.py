import frappe

# Function to create stock entry and call it by ajax call in js file

@frappe.whitelist()
def create_stock_entry(doc, event):
    print(doc.items[0].item_code)   
    # check if material request type is "Material Issue"  
    if(doc.material_request_type != "Material Issue"):
        return
    # Call Function From material request doctype in stock module
    from erpnext.stock.doctype.material_request.material_request import make_stock_entry
    new_stock_entry = make_stock_entry(doc.name)
    new_stock_entry.insert()
    new_stock_entry.submit()
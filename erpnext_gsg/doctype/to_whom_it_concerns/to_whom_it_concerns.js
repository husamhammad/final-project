// Copyright (c) 2023, huasm mahmoud hammad and contributors
// For license information, please see license.txt

frappe.ui.form.on('To Whom It Concerns', {
	employee:function(frm){
		frm.trigger('get_salary_slip');
	},
	// Ajax Call 
	get_salary_slip: function(frm){
		frappe.call({
			method:"erpnext_gsg.erpnext_gsg.doctype.to_whom_it_concerns.to_whom_it_concerns.get_salary_slip",
			args:{
				employee:frm.doc.employee,
			},
			callback: (r)=>{
				frm.doc.salary = r.message
				frm.refresh()
			}

		})
	}
});

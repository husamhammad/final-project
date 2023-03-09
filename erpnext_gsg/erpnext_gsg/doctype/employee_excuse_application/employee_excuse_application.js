// Copyright (c) 2023, huasm mahmoud hammad and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee Excuse Application', {
	// refresh: function(frm) {

	// }
	from_time:function(frm){
		frm.trigger('get_hours');
	},
	to_time:function(frm){
		frm.trigger('get_hours');
	},
	get_hours: function(frm){
		if((!frm.doc.from_time | !frm.doc.to_time )){
			return;
		}
		frappe.call({
			method:"erpnext_gsg.erpnext_gsg.doctype.employee_excuse_application.employee_excuse_application.clac_hours",
			args:{
				from_time:frm.doc.from_time,
				to_time:frm.doc.to_time	
			},
			callback: (r)=>{
				frm.doc.hours = r.message
				frm.refresh()
			}

		})
	}
});

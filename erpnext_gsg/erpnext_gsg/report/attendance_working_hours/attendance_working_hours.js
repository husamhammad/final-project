// Copyright (c) 2023, huasm mahmoud hammad and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Attendance Working Hours"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.add_months(frappe.datetime.get_today(), -1),
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"width": "80",
			"reqd": 1,
			"default": frappe.datetime.get_today()
		},
		{
			"fieldname":"employee",
			"label": __("Employee"),
			"fieldtype": "Link",
			"options": "Employee",
			"width": "80",
		},
		{
			"fieldname":"department",
			"label": __("Department"),
			"fieldtype": "Link",
			"options": "Department",
			"width": "80",
		},
		

	]
};
// frappe.templates["my_template_name"] = " \
//     <div class='form-group'> \
//         <label class='control-label' for='my_field_name'>My Field Label</label> \
//         <div class='controls'> \
//             <input type='text' class='form-control' id='my_field_name' name='my_field_name' data-fieldtype='Data' /> \
//         </div> \
//     </div>";
	
frappe.ui.form.on('Attendance Working Hours', {
	employee: function(frm) {
		// frm.set_input(frm.doc.name, null, 'Text', null, null, null, null, null, { target: '_blank' });
		console.log("*"*100)
		// print(frm.doc.name)
	}
  });

frappe.ui.form.on('Attendance Working Hours', {
    refresh: function(frm) {
        // Add HTML attributes to a link in the report
		print("*"*100)
        frm.fields_dict['name'].get_query = function(doc) {
            return {
                filters: {
                    'doctype': 'Attendance',
                    'fieldname': 'name',
                    'link': '<a href="/app/attendance/HR-ATT-2023-00001" data-doctype="Attendance" data-name="HR-ATT-2023-00001" data-value="HR-ATT-2023-00001" target="_blank>HR-ATT-2023-00001</a>'
					
                }
            };
        };
    }
});
# Copyright (c) 2023, huasm mahmoud hammad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ToWhomItConcerns(Document):
	pass

@frappe.whitelist()	
def get_salary_slips(employee):
	last_salary_slip = frappe.db.get_list('Salary Slip',
		filters={
			'employee': employee
		},
		fields=['base_gross_pay', 'posting_date'],
		order_by='posting_date desc',
		)
	return last_salary_slip[0].base_gross_pay


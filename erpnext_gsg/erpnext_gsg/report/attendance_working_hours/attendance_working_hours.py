# Copyright (c) 2023, huasm mahmoud hammad and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import date_diff
from frappe.utils import get_url, sanitize_html
from bs4 import BeautifulSoup




def execute(filters=None):
	columns, data = [], []
	conditions = get_conditions(filters)
	data = get_data(conditions,filters)
	# data = add_link(data)
	columns = get_columns()
	return columns, data


def get_conditions(filters):
	conditions = ""
	if filters.get("from_date") and filters.get("to_date"):
		conditions += "attendance_date between %(from_date)s and %(to_date)s"

	if filters.get("employee"):
		conditions += " and employee = %(employee)s"

	if filters.get("department"):
		conditions += " and department = %(department)s"

	return conditions

def get_columns():
	columns = [
		{'fieldname': 'employee', 'label':'Employee', 'fieldtype':'Link', 'options':'Employee'},
		{'fieldname': 'employee_name', 'label':'Employee Name', 'fieldtype':'Data'},
		{'fieldname': 'attendance_date', 'label':'Attendance Date', 'fieldtype':'Date'},
		{'fieldname': 'check_in', 'label':'Check In ', 'fieldtype':'Time'},
		{'fieldname': 'check_out', 'label':'Check Out', 'fieldtype':'Time'},
		{'fieldname': 'hours', 'label':'Working Hours', 'fieldtype':'Data'},
		{'fieldname': 'name', 'label':'View Attendance', 'fieldtype':'Link', 'options':'Attendance'},
	]
	return columns


def get_data(conditions, filters):
	data = frappe.db.sql(
		"""
		SELECT
			attendance_date, employee ,employee_name, check_in, check_out, hours, name FROM `tabAttendance` WHERE
			{conditions}
	""".format(
			conditions=conditions
		),
		filters,
		as_dict=1,
	)

	for i in data:
		link = frappe.utils.get_link_to_form("Attendance Working Hours", i.name)
		soup = BeautifulSoup(i.name, 'html.parser')
			# Add target="_blank" to the link
		soup.a['target'] = '_blank'
		print(link)
	return data

def add_target(data):
	
	for i in data:
		i.name = '<a href="/app/attendance/HR-ATT-2023-00001" data-doctype="Attendance" data-name="HR-ATT-2023-00001" data-value="HR-ATT-2023-00001" target="_blank">HR-ATT-2023-00001</a>'
		print(i)
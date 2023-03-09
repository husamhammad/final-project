frappe.ui.form.on("Journal Entry", {
    validate: function(frm) {
        if (frm.doc.__islocal) {
            frm.set_value('series', 'GSG-JV-.YYYY.-');
        }
    }
}
)
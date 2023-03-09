frappe.ui.form.on("Journal Entry", {
    refresh:function(){
        set_field_options("voucher_type", ["Journal Entry","Bank Entry", "Cash Entry", "Credit Card Entry", "Debit Note", "Credit Note", "Contra Entry", "Excise Entry", "Write Off Entry", "Opening Entry", "Depreciation Entry", "Exchange Rate Revaluation", "Exchange Gain Or Loss", "Deferred Revenue"])
    }
}
)
frappe.ui.form.on("Item Raw Materials", {
    custom_calculate_weight_kg:function(frm, cdt, cdn){
        let row = locals[cdt][cdn];
        frappe.call({
            method: "duckerp.duckerp.utils.item.weight_kg",
            args: { doc:frm.doc },
            callback: function(r) {
                if (r.message) {
                    frappe.model.set_value(cdt, cdn, "weight_in_kg", r.message);
                }
            }
        });
    }
})

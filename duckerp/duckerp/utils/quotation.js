frappe.ui.form.on("Quotation", {
    custom_fetch_items: function(frm) {
        if(frm.doc.custom_group_no){
            frappe.call({
                method: "duckerp.duckerp.utils.quotation.quotation_item_adding",
                args: { custom_group_no: frm.doc.custom_group_no, customer: frm.doc.party_name },
                callback: function(r) {
                    if (r.message) {
                        r.message.forEach((item) => {
                            let child = frm.add_child("items");
                            frappe.model.set_value(child.doctype, child.name, "item_code", item.item);
                            frappe.model.set_value(child.doctype, child.name, "custom_group_no", item.name);
                            frappe.model.set_value(child.doctype, child.name, "custom_group_name", item.part_group_name);
                        });
                        frm.refresh_field("items");
                    }
                }
            });
        }
    },
    party_name: function(frm){
       frm.clear_table("items");
    }
});
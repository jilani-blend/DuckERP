import frappe

@frappe.whitelist()
def quotation_item_adding(custom_group_no, customer):
    if custom_group_no and customer:
        part_no=frappe.db.get_value("Part Group", {"name":custom_group_no}, "part_group_name")
        if part_no:
            part_groups=frappe.db.get_all("Part Group", filters={"part_group_name":part_no, "customer_name":customer}, fields=["item", "name", "part_group_name"])
            return part_groups
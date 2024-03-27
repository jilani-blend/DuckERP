import frappe
import json
def weight_calculate(doc, action):
    if doc.custom_raw_materials:
        for i in doc.custom_raw_materials:
            if i.weight_formula:
                if "dia" in str(i.weight_formula):
                    if i.dia:
                        dia = float(i.dia or 0)
                    else:
                        frappe.throw("Dia Value is Empty")
                if "required_unit_lenght" in str(i.weight_formula):
                    if i.required_unit_lenght:
                        required_unit_lenght = float(i.required_unit_lenght or 0)                        
                    else:
                        frappe.throw("Required Unit Lenght Value is Empty")
                if "density" in str(i.weight_formula):
                    if i.density:
                        density = float(i.density or 0)
                    else:
                        frappe.throw("Density Value is Empty")
                if "thickness" in str(i.weight_formula):
                    if i.thickness:
                        thickness = float(i.thickness or 0)
                    else:
                        frappe.throw("Thickness Value is Empty")
                if "width" in str(i.weight_formula):
                    if i.width:
                        width = float(i.width or 0)
                    else:
                        frappe.throw("Width Value is Empty")
                weight_formula = i.weight_formula.format(**locals())
                weight_kg = eval(weight_formula)
                weight_kg = round(weight_kg, 3)
                i.weight_in_kg = weight_kg

@frappe.whitelist()
def weight_kg(doc):
    doc=json.loads(doc)
    if doc.get('custom_raw_materials'):
        for i in doc.get('custom_raw_materials'):
            if i.get('weight_formula'):
                if "dia" in str(i.get('weight_formula')):
                    if i.get('dia'):
                        dia = float(i.get('dia') or 0)
                    else:
                        frappe.throw("Dia Value is Empty")
                if "required_unit_lenght" in str(i.get('weight_formula')):
                    if i.get('required_unit_lenght'):
                        required_unit_lenght = float(i.get('required_unit_lenght') or 0)
                    else:
                        frappe.throw("Required Unit Lenght Value is Empty")
                if "density" in str(i.get('weight_formula')):
                    if i.get('density'):
                        density = float(i.get('density') or 0)
                    else:
                        frappe.throw("Density Value is Empty")
                if "thickness" in str(i.get('weight_formula')):
                    if i.get('thickness'):
                        thickness = float(i.get('thickness') or 0)
                    else:
                        frappe.throw("Thickness Value is Empty")
                if "width" in str(i.get('weight_formula')):
                    if i.get('width'):
                        width = float(i.get('width') or 0)
                    else:
                        frappe.throw("Width Value is Empty")
                weight_formula = i.get('weight_formula').format(**locals())
                weight_kg = eval(weight_formula)
                weight_kg = round(weight_kg, 3)
        return weight_kg

                

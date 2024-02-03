import frappe
import json
from frappe.utils import flt
@frappe.whitelist()
def return_invoices(doc):
    data = json.loads(doc)
    data["is_return"] = 1
    data["total"] = data["total"] * -1
    data["write_off_amount"] = 0
    # data["rounded_total"] = data["total"]
    data["grand_total"] = data["total"]
    # data["discount_amount"] = data["discount_amount"] * -1
    # data["base_total"] = data["total"]
    # data["base_grand_total"] = data["total"]
    # data["net_total"] = data["total"]
    invoice = frappe.new_doc("Sales Invoice")
    total = 0
    for item in data["items"]:
        item["qty"] = item["qty"] * -1
        item["amount"] = item["amount"] * -1
        total += item["qty"]
        item["base_amount"] = item["amount"]

    data["total_qty"] = total
    data["payments"][0]["amount"] = data["total"]
        # item["stock_qty"] = item["stock_qty"] * -1
    invoice.update(data)
    invoice.save()
    invoice.submit()
    return invoice

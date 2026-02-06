import frappe
from frappe import _

no_cache = 1

def get_context(context):
    if not frappe.session.user or frappe.session.user == "Guest":
        frappe.throw(_("You need to login"))

    contact = frappe.db.get_value(
        "Contact", {"user": frappe.session.user}, "name"
    )

    if not contact:
        context.invoices = []
        return context

    customers = frappe.get_all(
        "Dynamic Link",
        filters={
            "parenttype": "Contact",
            "parent": contact,
            "link_doctype": "Customer"
        },
        pluck="link_name"
    )

    if not customers:
        context.invoices = []
        return context

    context.invoices = frappe.get_all(
        "Sales Invoice",
        filters={
            "customer": ["in", customers],
            "docstatus": 1
        },
        fields=[
            "name",
            "posting_date",
            "due_date",
            "grand_total",
            "outstanding_amount",
            "status",
            "currency"
        ],
        order_by="posting_date desc"
    )

    return context

from erpnext.accounts.doctype.sales_invoice import sales_invoice as erpnext_sales_invoice

def get_list_context(context=None):
    # call ERPNext's original portal logic
    ctx = erpnext_sales_invoice.get_list_context(context)

    # override sorting for portal invoice list
    ctx["order_by"] = "posting_date desc, name desc"

    return ctx

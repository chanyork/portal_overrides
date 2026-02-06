from erpnext.accounts.doctype.sales_invoice.sales_invoice import get_list_context as original

def get_list_context(context=None):
    context = original(context)
    context.order_by = "posting_date desc, name desc"
    return context

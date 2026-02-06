from erpnext.controllers.website_list_for_contact import (
    get_transaction_list as original_get_transaction_list,
)

def get_transaction_list(
    doctype,
    txt=None,
    filters=None,
    limit_start=0,
    limit_page_length=20,
    order_by="modified",
    custom=False,
):
    # Force portal /invoices ordering to Posting Date (newest first)
    if doctype == "Sales Invoice":
        order_by = "posting_date desc, name desc"

    return original_get_transaction_list(
        doctype,
        txt=txt,
        filters=filters,
        limit_start=limit_start,
        limit_page_length=limit_page_length,
        order_by=order_by,
        custom=custom,
    )

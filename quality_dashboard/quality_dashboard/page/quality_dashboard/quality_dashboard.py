import frappe

@frappe.whitelist()
def get_quality_dashboard_data(customer=None, design=None, size=None, article=None):
    filters = {}

    # Add filters for the parent doctype
    if customer:
        filters['customer'] = customer
    if design:
        filters['design'] = design
    if size:
        filters['size'] = size
    if article:
        filters['article'] = article

    # Fetch the parent documents matching the filters
    parent_docs = frappe.db.get_all(
        "Daily Checking",
        filters=filters,
        fields=["name"]
    )

    # If no parent documents match, return an empty list
    if not parent_docs:
        return []

    # Extract the parent document names
    parent_names = [doc["name"] for doc in parent_docs]

    # Fetch data from the child table for the matched parent documents
    child_data = frappe.db.get_all(
        "Daily Checking Inspection CT",
        filters={"parent": ("in", parent_names)},
        fields=["parent", "major", "minor", "critical", "checker_name", "audit_qty"]
    )

    return child_data

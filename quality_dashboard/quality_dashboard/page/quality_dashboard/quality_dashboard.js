frappe.pages['quality-dashboard'].on_page_load = function (wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'Quality Dashboard',
        single_column: true,
    });

    // Add a section for filters
    page.add_field({
        label: 'Customer',
        fieldname: 'customer',
        fieldtype: 'Link',
        options: 'Customer',
        change: function () {
            load_data();
        }
    });

    function load_data() {
        frappe.call({
            method: "quality_dashboard.quality_dashboard.page.quality_dashboard.quality_dashboard.get_quality_dashboard_data",
            args: {
                customer: page.fields_dict.customer.value,
            },
            callback: function (r) {
                if (r.message) {
                    render_dashboard(r.message);
                }
            }
        });
    }

    function render_dashboard(data) {
        console.log(data); // Use this to debug
        // Clear previous content and render tables
    }

    // Initial load
    load_data();
};

app_name = "portal_overrides"
app_title = "Portal Overrides"
app_publisher = "York"
app_description = "Portal behavior customizations"
app_email = "chanyork@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "portal_overrides",
# 		"logo": "/assets/portal_overrides/logo.png",
# 		"title": "Portal Overrides",
# 		"route": "/portal_overrides",
# 		"has_permission": "portal_overrides.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/portal_overrides/css/portal_overrides.css"
# app_include_js = "/assets/portal_overrides/js/portal_overrides.js"

# include js, css files in header of web template
# web_include_css = "/assets/portal_overrides/css/portal_overrides.css"
# web_include_js = "/assets/portal_overrides/js/portal_overrides.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "portal_overrides/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "portal_overrides/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "portal_overrides.utils.jinja_methods",
# 	"filters": "portal_overrides.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "portal_overrides.install.before_install"
# after_install = "portal_overrides.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "portal_overrides.uninstall.before_uninstall"
# after_uninstall = "portal_overrides.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "portal_overrides.utils.before_app_install"
# after_app_install = "portal_overrides.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "portal_overrides.utils.before_app_uninstall"
# after_app_uninstall = "portal_overrides.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "portal_overrides.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"portal_overrides.tasks.all"
# 	],
# 	"daily": [
# 		"portal_overrides.tasks.daily"
# 	],
# 	"hourly": [
# 		"portal_overrides.tasks.hourly"
# 	],
# 	"weekly": [
# 		"portal_overrides.tasks.weekly"
# 	],
# 	"monthly": [
# 		"portal_overrides.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "portal_overrides.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "portal_overrides.event.get_events"
# }
override_whitelisted_methods = {
    "erpnext.accounts.doctype.sales_invoice.sales_invoice.get_list_context":
        "portal_overrides.portal_overrides.sales_invoice.get_list_context",

    "erpnext.controllers.website_list_for_contact.get_transaction_list":
        "portal_overrides.portal_overrides.website_list_for_contact.get_transaction_list",
}


#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "portal_overrides.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["portal_overrides.utils.before_request"]
# after_request = ["portal_overrides.utils.after_request"]

# Job Events
# ----------
# before_job = ["portal_overrides.utils.before_job"]
# after_job = ["portal_overrides.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"portal_overrides.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []


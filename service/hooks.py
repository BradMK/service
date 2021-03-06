app_name = "service"
app_title = "Service Management"
app_publisher = "www.ossph.com"
app_description = "Service Management"
app_icon = "icon-truck"
app_color = "orange"
app_email = "info@ossph.com"
app_version = "0.0.1"

update_website_context = "erpnext.shopping_cart.utils.update_website_context"
my_account_context = "erpnext.shopping_cart.utils.update_my_account_context"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/service/css/service.css"
# app_include_js = "/assets/service/js/service.js"

# include js, css files in header of web template
# web_include_css = "/assets/service/css/service.css"
# web_include_js = "/assets/service/js/service.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website
#fixtures = ["Web Form"]

#website_generators = ["Repair Order"]

website_route_rules = [
	{"from_route": "/repair_order", "to_route": "Repair Order"}, 
	{"from_route": "/repair_order/<path:name>", "to_route": "repair_order",
		"defaults": {
			"doctype": "Repair Order",
			"parents": [{"title": "Repair Order", "name": "repair_order"}]
		}
	}
]

portal_menu_items = [
	{"title": "Repair Orders", "route": "/repair_order", "reference_doctype": "Repair Order"}
]

has_website_permission = {
	"Repair Order": "erpnext.controllers.website_list_for_contact.has_website_permission"}



# ----------



# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "service.install.before_install"
# after_install = "service.install.after_install"

# Calendar
calendars = ["Appointment","Job Control"]

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "service.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.core.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.core.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"service.tasks.all"
# 	],
# 	"daily": [
# 		"service.tasks.daily"
# 	],
# 	"hourly": [
# 		"service.tasks.hourly"
# 	],
# 	"weekly": [
# 		"service.tasks.weekly"
# 	]
# 	"monthly": [
# 		"service.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "service.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.core.doctype.event.event.get_events": "service.event.get_events"
# }


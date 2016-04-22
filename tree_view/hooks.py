# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "tree_view"
app_title = "Tree View"
app_publisher = "MN Tech"
app_description = "Tree View Test"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "revant@revant.me"
app_version = "0.0.1"
app_license = "GPL v3"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/tree_view/css/tree_view.css"
# app_include_js = "/assets/tree_view/js/tree_view.js"

# include js, css files in header of web template
# web_include_css = "/assets/tree_view/css/tree_view.css"
# web_include_js = "/assets/tree_view/js/tree_view.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "tree_view.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "tree_view.install.before_install"
# after_install = "tree_view.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "tree_view.notifications.get_notification_config"

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
# 		"tree_view.tasks.all"
# 	],
# 	"daily": [
# 		"tree_view.tasks.daily"
# 	],
# 	"hourly": [
# 		"tree_view.tasks.hourly"
# 	],
# 	"weekly": [
# 		"tree_view.tasks.weekly"
# 	]
# 	"monthly": [
# 		"tree_view.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "tree_view.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "tree_view.event.get_events"
# }

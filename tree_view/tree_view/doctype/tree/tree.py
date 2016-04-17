# -*- coding: utf-8 -*-
# Copyright (c) 2015, MN Tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class Tree(Document):

	def on_update(self):
		self.update_nsm_model()

	def on_trash(self):
		self.update_nsm_model()
		self.validate_trash()

	def validate_trash(self):
		"""checks if child exists"""
		if not self.parent_tree:
			frappe.throw(_("Root Tree can not be deleted"))

		if self.check_if_child_exists():
			frappe.throw(_("Child tree exists for this tree. You can not delete this tree."))

	def update_nsm_model(self):
		"""update lft, rgt indices for nested set model"""
		import frappe
		import frappe.utils.nestedset
		frappe.utils.nestedset.update_nsm(self)

	def check_if_child_exists(self):
		return frappe.db.sql("""select name from `tabTree` where parent_tree = %s
			and docstatus != 2""", self.name)

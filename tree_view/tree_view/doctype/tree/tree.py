# -*- coding: utf-8 -*-
# Copyright (c) 2015, MN Tech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils.nestedset import NestedSet

class Tree(NestedSet):
	nsm_parent_field = 'parent_tree'

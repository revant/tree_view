from frappe import _

def get_data():
	return [
		{
			"label": _("Sample Tree App"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Tree",
					"description": _("Sample Tree."),
				}
			]
		},
		{
			"label": _("Chart Browser"),
			"icon": "icon-list",
			"items": [
				{
					"type": "page",
					"name": "Tree Browser",
					"label": _("Tree Browser"),
					"icon": "icon-bar-chart",
				},
			]
		},
	]

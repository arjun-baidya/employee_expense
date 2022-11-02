# -*- coding: utf-8 -*-
{
    'name': 'Employee Expense',
    'version': '15.0.0',
    'website': '',
    'category': '',
    'summary': '',
    'description': """ test """,
    'depends': ['base', 'mail', 'hr', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/travel_expense.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

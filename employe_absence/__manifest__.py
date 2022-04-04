# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Absences',
    'version': '1.1',
    'category': 'Human Resources/Absences',
    'sequence': 95,
    'summary': 'Absence des employés',
    'description': "",
    'depends': [
        'hr'

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/motif_absence_views.xml',
        'views/affecter_absence_views.xml',
        'views/menu.xml',





    ],
    'demo': [

    ],

    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {


    },
    'license': 'LGPL-3',
}
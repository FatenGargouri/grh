# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Rapports',
    'version': '1.1',
    'category': 'Human Resources/Rapports',
    'sequence': 95,
    'summary': 'Rapport des employés',
    'description': "",
    'depends': [
        'base',
        'mail',
        'hr',
        'hr_attendance'

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/form_views.xml',
        'views/rapport_template_views.xml',
        'views/rapport_views.xml',
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
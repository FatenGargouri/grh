# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'horaires',
    'version': '1.1',
    'category': 'Human Resources/horaires',
    'sequence': 95,
    'summary': 'Horaire des employés',
    'description': "",
    'depends': [
        'base',
        'mail'

    ],
    'data': [
        'security/ir.model.access.csv',
        'views/table_horaire_views.xml',
        'views/horaire_travail_views.xml',
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
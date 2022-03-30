# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Congés des Employés',
    'version': '1.1',
    'category': 'Human Resources/congés',
    'sequence': 95,
    'summary': 'Centralize congés information',
    'description': "",
    'website': 'https://www.odoo.com/app/employees',
    'images': [
        'static/description/icon.png'

    ],
    'depends': [
        'hr',
        'hr_holidays'
    ],
    'data': [

        'views/conges_views.xml',





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

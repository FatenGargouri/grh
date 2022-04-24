# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Présences des employés',
    'version': '1.1',
    'category': 'Human Resources/Présences',
    'sequence': 95,
    'summary': 'Présences des employés',
    'description': "",
    'depends': [
        'base',
        'hr',
        'hr_attendance'
    ],
    'data': [
        'views/presence_views.xml',




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
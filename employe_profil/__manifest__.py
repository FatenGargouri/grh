# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employees profils',
    'version': '1.1',
    'category': 'Human Resources/Profils',
    'sequence': 95,
    'summary': 'Centralize employee information',
    'description': "",
    'website': 'https://www.odoo.com/app/employees',
    'images': [
        'static/description/icon.png'

    ],
    'depends': [
        'hr'
    ],
    'data': [

        'views/profil_user_views.xml',





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

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'contrats',
    'version': '1.1',
    'category': 'Human Resources/Contracts',
    'sequence': 95,
    'summary': 'Contrats des employés',
    'description': "",
    'website': 'https://www.odoo.com/app/employees',
    'depends': [
        'base',
        'hr',
        'hr_contract'
    ],
    'data': [
        'views/contract_view.xml',



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
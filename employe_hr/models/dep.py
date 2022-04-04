# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class HrDepartment(models.Model):
    """
        HrDepartment est une classe qui permet l'héritage de hr.departement  pour faire des changements .
    """

    _inherit = "hr.department"









# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models,_


class HrAllocation(models.Model):
    """
    NB: description de la classe
    """
    _inherit = "hr.leave.allocation"
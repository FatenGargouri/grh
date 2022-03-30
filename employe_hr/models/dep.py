# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class HrDepartment(models.Model):

    _inherit = "hr.department"

    #sous_dep = fields.One2many('hr.department','parent_id',string="Sous département")







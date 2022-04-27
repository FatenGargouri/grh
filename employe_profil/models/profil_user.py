# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
import re


class HrProfil(models.Model):
    """
    HrEmployee est une classe qui permet l'héritage de hr.employee pour faire des changements .
    """
    _inherit = "res.users"

    adresse = fields.Char(related='employee_id.adresse', readonly=False, related_sudo=False)

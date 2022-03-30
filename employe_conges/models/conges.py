# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models,_


class HrConges(models.Model):
    """
    NB: description de la classe
    """
    _inherit = "hr.leave"

    nature = fields.Char(string="Nature et motif de congés")
    contact = fields.Char(string="Contact pendant le congés")
    adresse = fields.Char(string="Adresse")
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class hr_planing(models.Model):
    _name = "hr.planing"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Planing"

    departement = fields.Many2one("hr.department",string="Département")
    employe = fields.Many2many("hr.employee",string="Employé")
    tableau_horaire = fields.Many2one("hr.table.horaire",string="Tableau horaire")
    debut = fields.Date(string="De")
    fin = fields.Date(string="à")





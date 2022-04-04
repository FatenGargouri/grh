# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class MotifAbsence(models.Model):
    _name = "motif.absence"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    """
         Motif absence est une classe qui permet de voir les motifs absences .
    """

    name = fields.Char(string="motif")
    justification=fields.Selection([
        ('oui', 'Oui'),
        ('non', 'Non')], string='Justification', default='oui')
    nombre_jours = fields.Integer(string="Nombre de jours")
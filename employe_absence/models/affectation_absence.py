# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _



class AffectationAbsence(models.Model):
    _name = "affectation.absence"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    """
         Motif absence est une classe qui permet de voir les motifs absences .
    """

    employe = fields.Many2one("hr.employee" , string="employe")
    date_debut = fields.Date(string="Début date")
    date_fin = fields.Date(string="Fin date")
    debut = fields.Float(string='Début')
    fin = fields.Float(string='Fin')
    motif = fields.Many2one("motif.absence",string="Motif absence")
    raison = fields.Char(string="Raison absence")



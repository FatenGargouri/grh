# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class hr_horaire_travail(models.Model):
    _name = "hr.horaire.travail"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Horaire de travail"

    name = fields.Char(string="Horaire")
    marge_retard = fields.Integer(string="Marge de retard (min)")
    marge_dp_anticipe = fields.Integer(string="Marge dp anticipé (min)")
    jours_travailles = fields.Integer(string="Jours travaillés")
    repos = fields.Integer(string="Repos (min)")

    debut = fields.Float(string='Début')
    fin = fields.Float(string='Fin')
    debut_entree = fields.Float(string='Début entrée')
    fin_entree = fields.Float(string='Fin entrée')
    debut_sortie = fields.Float(string='Début sortie')
    fin_sortie = fields.Float(string='Fin sortie')
















# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class hr_table_horaire(models.Model):
    _name = "hr.table.horaire"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Tableau horaire"



    name = fields.Char(string="Nom tableau", required=True)
    lundi = fields.Many2one('hr.horaire.travail', string='Lundi')
    mardi = fields.Many2one('hr.horaire.travail', string='Mardi')
    mercredi = fields.Many2one('hr.horaire.travail', string='Mercredi')
    jeudi = fields.Many2one('hr.horaire.travail', string='Jeudi')
    vendredi = fields.Many2one('hr.horaire.travail', string='Vendredi')
    samedi = fields.Many2one('hr.horaire.travail', string='Samedi')
    dimanche = fields.Many2one('hr.horaire.travail', string='Dimanche')


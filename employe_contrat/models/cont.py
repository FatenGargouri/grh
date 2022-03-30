# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_
from odoo.exceptions import ValidationError

class ContractEmploye(models.Model):
    """
      NB: description de la classe
    """

    _inherit = 'hr.contract',

    demarrage = fields.Date('Date de démarrage', tracking=True)
    rappel1 = fields.Date('Date rappel1', tracking=True)
    rappel2 = fields.Date('Date rappel2', tracking=True)
    type = fields.Selection([
        ('stagiaire', 'Stagiaire'),
        ('civp1', 'Civp1'),
        ('civp2', 'Civp2'),
        ('cdi', 'Cdi'),
        ('cdd', 'CDD'),
        ('cdi_karama', 'CDI KARAMA'),
        ('autres', 'Autres')
    ], string='Type contrat', tracking=True)
    validite = fields.Selection([('ok', 'OK'), ('non', 'NON'), ('en cours', 'En cours')], string="Validité préavis")

    @api.constrains('name')
    def _check_name(self):
        for employee in self:
            if employee.name and not (employee.name.isdigit()):
                raise ValidationError("Le champ référence doit contenir que des nombres")


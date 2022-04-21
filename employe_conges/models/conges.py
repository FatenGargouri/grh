# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models,_
from datetime import date, datetime, time
from odoo.exceptions import ValidationError


class HrConges(models.Model):
    """
    NB: description de la classe
    """
    _inherit = "hr.leave"

    nature = fields.Char(string="Nature et motif de congés")
    contact = fields.Char(string="Contact pendant le congés")
    adresse = fields.Char(string="Adresse")

    @api.constrains('date_from')
    def _check_date_from(self):
        date_from = self.date_from
        dateToday = datetime.today()
        if date_from < dateToday:
            raise ValidationError("La champ (partir de) doit etre supérieur ou égale à date d'aujourd'hui")

class TypeConges(models.Model):
    """
    NB: description de la classe
    """
    _inherit = "hr.leave.type"


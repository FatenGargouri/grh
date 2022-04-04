# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models,_

class ContractHistoryEmployee(models.Model):
    """
      Héritage de la classe contract
    """

    _inherit = 'hr.contract.history',



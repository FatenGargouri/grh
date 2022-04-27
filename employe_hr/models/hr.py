# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_
from odoo.exceptions import ValidationError
import re


class HrEmployee(models.Model):
    """
    HrEmployee est une classe qui permet l'héritage de hr.employee pour faire des changements .
    """
    _inherit = "hr.employee"

    #les champs ajoutés à la classe HrEmployee
    matricule = fields.Char(string="Matricule")
    cin = fields.Char(string="Cin",size=8)
    cnss = fields.Char(string="CNSS" ,size=5)
    activite = fields.Selection([
        ('direct', 'Direct'),
        ('indirect', 'Indirect')], string='Activité',default='direct', tracking=True)
    teletravail = fields.Selection([
        ('oui', 'Oui'),
        ('non', 'Non')], string='Télétravail',default='non', tracking=True)
    adresse = fields.Char(string="Adresse")
    role = fields.Selection([
        ('collaborateur', 'Collaborateur'),
        ('chef equipe', 'Chef équipe'),
        ('responsable rh', 'Responsable RH'),
        ('directeur société', 'Directeur société'),
        ('pdg', 'PDG'),
    ], string='Role', tracking=True)
    solde = fields.Integer(string="Solde congés")

    #La relation Many2One entre la classe hr et la classe hr.table.horaire
    tableau_horaire = fields.Many2one("hr.table.horaire",string="Tableau horaire")

    # Un controle pour le champ matricule doit etre existe dans la base et ne contient que des nombres .
    @api.constrains('matricule')
    def _check_matricule(self):
       for employee in self:
            if employee.matricule and not (employee.matricule.isdigit()):
                raise ValidationError("Le champ matricule doit contenir que des nombres")

    # Un controle pour le champ cin doit etre existe dans la base et ne contient que des nombres .
    @api.constrains('cin')
    def _check_cin(self):
        for employee in self:
            if employee.cin and not (employee.cin.isdigit()):
               raise ValidationError("Le champ cin doit contenir que des nombres")

    # Un controle pour le champ mobile_phone doit etre existe dans la base et ne contient que des nombres .
    @api.constrains('mobile_phone')
    def _check_mobile_phone(self):
        for employee in self:
            if employee.mobile_phone and not (employee.mobile_phone.isdigit()):
                raise ValidationError("Le champ Téléphone doit contenir que des nombres")

    # Un controle pour le champ work_email doit etre existe dans la base et  contient le symbole @ .
    @api.constrains('work_email')
    def _check_work_email(self):
        for employee in self:
            regex = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
            if employee.work_email and not (re.search(regex, employee.work_email)):
                raise ValidationError("Invalid Email")

    # Un controle pour le champ cnss doit etre existe dans la base et ne contient que des nombres .
    @api.constrains('cnss')
    def _check_cnss(self):
        for employee in self:
            if employee.cnss and not (employee.cnss.isdigit()):
                raise ValidationError("Le champ cnss doit contenir que des nombres")

























# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, time
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from pytz import timezone
from calendar import calendar


class RapportSynthese(models.TransientModel):
    _name = 'rapport.synthese'
    _description = "Rapport synthèses des employés"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2many('hr.employee', string="Employee")
    from_date = fields.Date(string= 'Date début', default=lambda self: fields.Date.to_string(date.today()),required=True)
    to_date = fields.Date(string="Date fin",required=True)

    def print_report(self):
        domain = []
        datas = []
        jour_ferier=[]
        if self.employee_id:
            domain.append(('id', '=', self.employee_id.ids))

        employees = self.env['hr.employee'].search(domain)
        for employee in employees:
            present = 0
            absent = 0
            tz = timezone(employee.resource_calendar_id.tz)
            date_from = tz.localize(datetime.combine(fields.Datetime.from_string(str(self.from_date)), time.min))
            date_to = tz.localize(datetime.combine(fields.Datetime.from_string(str(self.to_date)), time.max))
            intervals = employee.list_work_time_per_day(date_from, date_to, calendar=employee.resource_calendar_id)
            for rec in intervals:
                attendances = self.env["hr.attendance"].search(
                    [('employee_id', '=', employee.id), ('check_in', '>=', rec[0]),
                     ('check_in', '<=', rec[0])])
                if attendances:
                    present += 1
                else:
                    absent += 1

                jour_ferier = self.env["hr.leave.report.calendar"].search(
                    [('name', '>=',rec[0])])
                if jour_ferier:
                    jour_ferier += 1



            datas.append({
                'id': employee.id,
                'name': employee.name,
                'jours ferier' : jour_ferier,
                'present': present,
                'absent': absent,
            })
        res = {
            'attendances': datas,
            'start_date': self.from_date,
            'end_date': self.to_date,
        }
        data = {
            'form': res,
        }







        return self.env.ref('employe_rapport.rapport_synthese').report_action([],data=data)

    @api.constrains('date_from','to_date')
    def _check_date(self):
        from_date = self.from_date
        to_date = self.to_date
        if from_date > to_date:
            raise ValidationError("Date début doit inférieur à date fin")










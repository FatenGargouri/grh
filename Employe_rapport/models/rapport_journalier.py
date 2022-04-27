# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, time , timedelta
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
from pytz import timezone


class RapportJournalier(models.TransientModel):
    _name = 'rapport.journalier'
    _description = "Rapport journalier des employés"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    employee_id = fields.Many2many('hr.employee', string="Employee")
    from_date = fields.Date(string='Date début', default=lambda self: fields.Date.to_string(date.today()),required=True)
    to_date = fields.Date(string="Date fin",required=True)

    def print_report(self):
        domain = []
        datas = []
        if self.employee_id:
            domain.append(('id', '=', self.employee_id.ids))

        employees = self.env['hr.employee'].search(domain)
        for employee in employees:
            supp =0
            tz = timezone(employee.resource_calendar_id.tz)
            date_from = tz.localize(datetime.combine(fields.Datetime.from_string(str(self.from_date)), time.min))
            date_to = tz.localize(datetime.combine(fields.Datetime.from_string(str(self.to_date)), time.max))
            intervals = employee.list_work_time_per_day(date_from, date_to, calendar=employee.resource_calendar_id)
            
            #Indiquer si l'employé est présent ou absent .
            for rec in intervals:
                attendances = self.env["hr.attendance"].search(
                    [('employee_id', '=', employee.id), ('check_in', '>=', rec[0]),
                     ('check_out', '<=', rec[0])])
                if attendances:
                    etat = "Present"
                else:
                    etat = "Absent"

                # # Calculer le retard
                # hours = self.env["res.config.settings"].search([])
                # if (attendances.check_in).time() > hours.hour_from:
                #     late = (attendances.check_in).time() - hours.hour_from
                # Calculer les departs anticipé
                # timesortie1 ="12:00:00"
                # timesortie2 ="17:00:00"
                # date_timesortie1 = datetime.strptime(timesortie1, '%H:%M:%S')
                # date_timesortie2 = datetime.strptime(timesortie2, '%H:%M:%S')
                # if attendances.check_out < date_timesortie1 or attendances.check_out < date_timesortie2:
                #     depart1 = date_timesortie1 - attendances.check_out
                #     depart2 = date_timesortie2 - attendances.check_out
                #     depart = depart1 + depart2


                # #Calculer les heures supplémentaires
                # if attendances.worked_hours > 8:
                #     supp = attendances.worked_hours-8

            datas.append({
                'date': intervals,
                'name': employee.name,
                'entre': attendances.check_in,
                'sortie': attendances.check_out,
                'worked_hours': attendances.worked_hours,
                # 'late': attendances.late_check_in,
                # 'depart': depart,
                # 'supp': supp,
                'etat': etat,
            })
        res = {
            'attendances': datas,
            'start_date': self.from_date,
            'end_date': self.to_date,
        }
        data = {
            'form': res,
        }

        return self.env.ref('employe_rapport.rapport_journalier').report_action([],data=data)






    @api.constrains('from_date','to_date')
    def _check_date(self):
        from_date = self.from_date
        to_date = self.to_date
        if from_date > to_date:
            raise ValidationError("Date début doit inférieur à date fin")










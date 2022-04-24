# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models,_
from datetime import date, datetime, time, timedelta
import pytz
from odoo.exceptions import ValidationError
import re


class HrPresence(models.Model):
    """
    HrPresence est une classe qui permet l'héritage de hr.employee pour faire des changements .
    """
    _inherit = "hr.attendance"

    late_check_in = fields.Integer(string="Late Check-in(Minutes)", compute="get_late_minutes")


    #Calculer les minutes retards
    def get_late_minutes(self):
        for rec in self:
            rec.late_check_in = 0.0
            week_day = rec.sudo().check_in.weekday()
            if rec.employee_id.contract_id:
                work_schedule = rec.sudo().employee_id.contract_id.resource_calendar_id
                for schedule in work_schedule.sudo().attendance_ids:
                    if schedule.dayofweek == str(week_day) and schedule.day_period == 'morning':
                        work_from = schedule.hour_from
                        result = '{0:02.0f}:{1:02.0f}'.format(*divmod(work_from * 60, 60))

                        user_tz = self.env.user.tz
                        dt = rec.check_in

                        if user_tz in pytz.all_timezones:
                            old_tz = pytz.timezone('UTC')
                            new_tz = pytz.timezone(user_tz)
                            dt = old_tz.localize(dt).astimezone(new_tz)
                        str_time = dt.strftime("%H:%M")
                        check_in_date = datetime.strptime(str_time, "%H:%M").time()
                        start_date = datetime.strptime(result, "%H:%M").time()
                        t1 = timedelta(hours=check_in_date.hour, minutes=check_in_date.minute)
                        t2 = timedelta(hours=start_date.hour, minutes=start_date.minute)
                        if check_in_date > start_date:
                            final = t1 - t2
                            rec.sudo().late_check_in = final.total_seconds() / 60



    # def test_cron_absence(self):
    #     values = []
    #     activity_type_id = self.env['mail.activity.type'].search([('name', '=', 'À faire')])
    #     print("bonjour")
        # Pointage sur le modele hr.employee et charger tous les employés
        # list_employee = self.env['hr.employee'].search([])
        # list_employee_present = []
        # dateToday = datetime.today().strftime("%Y-%m-%d")
        # date_time_obj = datetime.strptime(dateToday,'%Y-%m-%d')
        # current_date = date_time_obj.date()
        # for emps in self.search([]):
        #     check_in_c = emps.check_in.date()
        #     if check_in_c == current_date:
        #         # ajouter dans la liste
        #         list_employee_present.append(emps.employee_id)
        #
        # for empsa in list_employee_present:
        #     print(empsa.name)


        # absent_emp = list_employee_present.difference(list_employee_present)
        # print(absent_emp)
        # difference_1 = set(list_employee).difference(set(list_employee_present))
        # difference_2 = set(list_employee_present).difference(set(list_employee))
        #
        # list_difference = list(difference_1.union(difference_2))
        # print(list_difference)
        #
        # for i in list_difference:
        #     print(i.name)
        #     values.append({
        #         "activity_type_id": activity_type_id.id,
        #         "date_deadline": dateToday,
        #         "user_id": i.user_id.id,
        #         'summary': "Absences",
        #         'note': "Bonjour, cet employé est absent",
        #         "res_model_id": self.env['ir.model'].search([('model', '=', 'hr.attendance')]).id,
        #         "res_id": i.id,
        #     })
        #     self.env['mail.activity'].create(values)














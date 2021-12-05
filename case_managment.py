# -*- coding: utf-8 -*-
#############################################################################
#
#    Codesk Solutions L.L.C.
#
#    Copyright (C) 2021-TODAY Codesk solutions(<https://www.Codesksolutions.co>)
#    Author: Codesk Solutions(<https://www.Codesksolutions.co>)
#
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

    from odoo import models, fields

    class CaseManagment(models.Model):
        _name ='case.management'
        _discription ='the main moduel'
        pdb_number = fields.Intger(required=True)
        dsapp_number = fields.Intger()
        first_name = fields.Char()
        second_name = fields.Char()
        third_name = fields.Char()
        fourth_name = fields.Char()
        national_number = fields.Intger()
        primary_phone_number = fields.Char()
        secondary_phone_number = fields.Char()
        secondary_phone_number_owner = fields.Char()
        email = fields.Char()
        facebook = fields.Char()
        gender = fields.Selection([('male', 'male'),('male', 'male')])
        bod = fields.Date()
        martial_status = fields.Selection([('single', 'single'),('married', 'married'),('divorced /sperated away', 'divorced /sperated away')])
        have_children = fields.Boolean()
        number_of_childern = fields.Integer()
        detailed_address = fields.Text()
        address_url = fields.Char()
        reason_of_transfer = fields.Text()
        date_of_transfer = fields.Date()
        date_of_entry = fields.Date()
        notes_transfer = fields.Text()
        date_youth_camp = fields.Date()
        notes_youth_camp = fields.Text()
        date_semi_indepenacy = fields.Date()
        notes_semi_youth = fields.Text()
        illegal_acts = fields.Boolean()
        note_illegal_acts = fields.Text()
        date_illegal_acts = fields.Date()
        bio_family_available = fields.Selection([('yes/intgreated', 'yes/intgreated'),('yes/not intgrated', 'yes/not intgrated'),('N/A', 'N/A')])
        frq_bio_family_inter = fields.Selection([('always', 'always'),('rearly', 'rearly'),('Never with knowing the bio family', 'Never with knowing the bio family'),('Never dont know the bio family', 'Never dont know the bio family'),('Never and not allowed by court', 'Never and not allowed by court'),('no data', 'no data')])
        bros_out_sos = fields.Selection([('No', 'No'),('Yes', 'Yes'),('no available data', 'no available data')])
        is_gifted = fields.Float()
        needed_support = fields.Selection([('manamgent direct supervision', 'manamgent direct supervision'),('motivation inspireation', 'motivation inspireation'),('training directing', 'training directing'),('enablement task assignment', 'enablement task assignment')])
        personal_id_att = fields.Binary()
        birth_certifcate = fields.Binary()
        passport_att = fields.Binary()
        cv_att = fields.Binary()
        misc_attachment = fields.Binary()
        personal_pic = fields.Binary()
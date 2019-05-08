# -*- coding: utf-8 -*-

from odoo import models, fields, api,_

class user_wizard(models.Model):
    _name = 'user_wizard.user_wizard'
    _rec_name='first_name'
    primary_client = fields.Many2one('res.company',string="Primary Client",required=1)
    user_type=fields.Many2one('res.groups',string="User Type",required=1)
    first_name=fields.Char("Frist Name")
    last_name=fields.Char("Last Name")
    email=fields.Char("Email")
    login=fields.Char("Login")
    password=fields.Char("Password")
    open_user_setting=fields.Boolean("Open User Setting")

    @api.multi
    def create_field(self):
        if self.open_user_setting==1:
            return {
            'name': _('User'),
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'res.users',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }
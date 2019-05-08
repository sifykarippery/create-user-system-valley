# -*- coding: utf-8 -*-
from odoo import http

# class UserWizard(http.Controller):
#     @http.route('/user_wizard/user_wizard/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/user_wizard/user_wizard/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('user_wizard.listing', {
#             'root': '/user_wizard/user_wizard',
#             'objects': http.request.env['user_wizard.user_wizard'].search([]),
#         })

#     @http.route('/user_wizard/user_wizard/objects/<model("user_wizard.user_wizard"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('user_wizard.object', {
#             'object': obj
#         })
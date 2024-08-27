# -*- coding: utf-8 -*-
# from odoo import http


# class CustomWebTheme(http.Controller):
#     @http.route('/custom_web_theme/custom_web_theme', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_web_theme/custom_web_theme/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_web_theme.listing', {
#             'root': '/custom_web_theme/custom_web_theme',
#             'objects': http.request.env['custom_web_theme.custom_web_theme'].search([]),
#         })

#     @http.route('/custom_web_theme/custom_web_theme/objects/<model("custom_web_theme.custom_web_theme"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_web_theme.object', {
#             'object': obj
#         })


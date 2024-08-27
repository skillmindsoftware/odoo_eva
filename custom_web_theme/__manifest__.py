# -*- coding: utf-8 -*-
{
    'name': "Custom Web Theme",
    'summary': "A custom web theme for Odoo",
    'description': """
    This module provides a custom web theme for Odoo,
    including customized layout, styles, and website features.
    """,
    'author': "Edwin Mutua",
    'website': "https://www.yourcompany.com",
    'category': 'Website/Theme',
    'version': '17.0.1.0.0',
    'license': 'LGPL-3',
    'depends': ['website', 'website_sale'],
    'data': [
        'views/layout.xml',
        # 'views/homepage.xml',
        # 'views/snippets/snippets.xml',
    ],

    'assets': {
        'web._assets_primary_variables': [
            'custom_web_theme/static/src/scss/primary_variables.scss',
        ],
        # 'web._assets_frontend_helpers': [
        #     ('prepend', 'custom_web_theme/static/src/scss/bootstrap_overridden.scss'),
        # ],
        'web.assets_frontend': [
            'custom_web_theme/static/src/scss/theme.scss',
            # 'custom_web_theme/static/src/scss/product_card_snippet.scss',
            # 'custom_web_theme/static/src/js/custom_dynamic_snippet_carousel.js', 
        ],
    },
    # 'images': [
    #     'static/description/icon.png',
    # ],
    'application': False,
    'installable': True,
    'auto_install': False,
}
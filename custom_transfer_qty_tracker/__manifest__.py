{
    'name': 'Internal Transfer Quantity Tracker',
    'version': '17.0.1.0',
    'category': 'Inventory',
    'summary': 'Add available and remaining quantity info to internal transfers',
    'description': """
Internal Transfer Quantity Tracker
==================================
This module enhances internal transfers in Odoo by adding available and remaining quantity information.
Features:
- Displays available quantity for products in internal transfers
- Shows remaining quantity after transfer for each product
- Updates quantities in real-time as transfer details are modified
    """,
    'author': 'Edwin Mutua',
    'website': 'https://www.skillmindsoftware.com',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'assets': {},
    'images': [],
}
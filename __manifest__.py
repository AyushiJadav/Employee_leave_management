# -*- coding: utf-8 -*-
{
    # App information
    'name': 'Employee Leave Management',
    'category': 'Tools',
    'version': '18.0.1.0',
    'summary': 'Custom employee leaves management module.',
    'license': 'OPL-1',
    
    # Dependencies
    'depends': ['base','mail'],

    # Views
    'data': [
        'security/ir.model.access.csv',
        'views/leave_request.xml',
    ],

    # Author
    'author': 'Ayushi Jadav',
    'website': '',
    'maintainer': 'Ayushi Jadav',

    # Technical
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,

    # Store fields (optional, safe to keep but not needed locally)
    'images': [],
    'live_test_url': '',
    'price': 199,
    'currency': 'EUR',
}

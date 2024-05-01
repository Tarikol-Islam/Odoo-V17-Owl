# -*- coding: utf-8 -*-
{
    'name': "owl_components",

    'summary': "Basic Owl Components",

    'description': """
        Basic Owl Components, those are provide by built-in.
    """,

    'author': "Tarikol-Islam",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales/Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale','sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
    'assets': {
        'web.assets_backend': [
            'owl_components/static/src/**/*',
        ],
    },
}


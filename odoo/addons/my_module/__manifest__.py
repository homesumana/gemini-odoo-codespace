{
    'name': 'My REST API Module',
    'version': '1.0',
    'summary': 'A module to provide REST API endpoints.',
    'author': 'Gemini',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/my_module_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

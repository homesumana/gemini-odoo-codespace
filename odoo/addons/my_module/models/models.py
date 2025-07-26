from odoo import models, fields

class MyModuleModel(models.Model):
    _name = 'my_module.my_module'
    _description = 'My Module Model'

    name = fields.Char('Name')
    description = fields.Text('Description')

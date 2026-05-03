from odoo import models, fields

class LeaveType(models.Model):
    _name = 'leave.type'
    _description = 'Leave Type'

    name = fields.Char(String = 'Name', required = True)
    max_days = fields.Integer(String = 'Max Days')
    color = fields.Integer(String = 'Color')

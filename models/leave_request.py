from odoo import models, fields,api
from odoo.exceptions import ValidationError


class LeaveRequest(models.Model):
    _name = 'leave.request'

    employee_id = fields.Many2one('res.partner', string='Employee ID')
    leave_type_id = fields.Many2one('leave.type', string='Leave type id')
    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    reason = fields.Text(string='Reason')
    state = fields.Selection([('draft', 'draft'),
            ('submitted', 'submitted'),
            ('approved','approved'),
            ('rejected','rejected')],
            default = 'draft')
    duration_days = fields.Float(compute="_compute_days")
    rejected_reason = fields.Char(string='Rejection Reason', readonly=True)



    @api.constrains('date_from', 'date_to', 'leave_type_id')
    def check_days(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                if rec.date_to < rec.date_from:
                    raise ValidationError("End date must be after start date.")

            if rec.leave_type_id and rec.duration_days:
                if rec.duration_days > rec.leave_type_id.max_days:
                    raise ValidationError("Leave exceeds maximum allowed days.")
    @api.depends('date_from','date_to')    
    def _compute_days(self):
        for i in self:
            if i.date_to  and i.date_from:
                i.duration_days = (i.date_to - i.date_from).days + 1
            else:
                i.duration_days = 0

    def action_submit(self):
        for i in self:
            i.state = "submitted"

    def action_open_wizard(self):
        return{'type': 'ir.actions.act_window',
            'name': 'Leave Action Wizard',
            'res_model': 'leave.action.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_leave_id': self.id},
        }
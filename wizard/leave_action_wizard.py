from odoo import models, fields, api

class LeaveAction(models.TransientModel):
    _name = 'leave.action.wizard'
    _description = 'Leave action wizard'

    leave_id = fields.Many2one('leave.request', string = 'Leave ID')
    action_type = fields.Selection([('approved','approved'),('rejected','rejected')], String = 'Leave Action')
    note = fields.Text(String ="Note", required = True)
    rejection_reason = fields.Char(string = "Rejection reason")


    def confirm(self):
        for i in self:
            if i.action_type == "approved":
                i.leave_id.write({
                        'state':'approved',
                        'rejection_reason': False
                })
            else:
                i.leave_id.write({
                    'state':'rejected',
                    'rejected_reason': i.note
                })
            return {'type': 'ir.actions.act_window_close'}
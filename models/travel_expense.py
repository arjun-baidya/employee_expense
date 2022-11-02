from odoo import models, fields, api, _
from datetime import datetime


class TravelExpense(models.Model):
    _name = 'travel.expense'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Travel expense'
    # _rec_name = 'customer_name'

    employee_name = fields.Many2one('hr.employee', 'Employee Name')
    manager = fields.Many2one('hr.employee', string="Manager")
    department = fields.Many2one('hr.department', string="Department")
    departure_place = fields.Char(string="From")
    destination_place = fields.Char(string="To")
    departure_date_time = fields.Datetime(string="Departure Date-Time")
    destination_date_time = fields.Datetime(string="Destination Date-Time")
    travel_mode = fields.Char(string="Travel Mode")
    cash = fields.Selection([
        ('regular', 'Regular'),
        ('advance', 'Advance'),
    ], string='Cash', required=True)
    travel_expense_line_ids = fields.One2many('travel.expense.line', 'travel_expense_line_id', string="line ids")
    travel_log_ids = fields.One2many('travel.approve.line', 'travel_log_id', string="log ids")

    @api.onchange('employee_name')
    def onchange_dept(self):
        self.department = self.employee_name.department_id
        self.manager = self.employee_name.parent_id


class TravelExpenseLine(models.Model):
    _name = 'travel.expense.line'
    _description = " Travel Expense Line"

    date = fields.Datetime(string="Date")
    product = fields.Many2one('product.product', string="Product")
    qty = fields.Integer(string="Qty")
    uom = fields.Many2one('uom.uom', string="UOM")
    price = fields.Float(string="Price")
    tax = fields.Float(string="Tax")
    sub_total = fields.Float(string="Sub-Total")
    travel_expense_line_id = fields.Many2one('travel.expense', string="Line id")


class TravelExpenseLog(models.Model):
    _name = 'travel.approve.line'
    _description = " Travel"

    # for log section
    requested_by = fields.Many2one('res.user', string="Requested By")
    approved_by = fields.Many2one('hr.employee', string="Approved By")
    requested_date = fields.Datetime(string="Requested Date")
    approved_date = fields.Datetime(string="Approved Date")
    travel_log_id = fields.Many2one('travel.expense', string="log id")


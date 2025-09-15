from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    marca = fields.Char(string="Marca")
    numero = fields.Integer(string="Número", required=True)

    _sql_constraints = [
        ("numero_unique", "unique(numero)", "El número debe ser único."),
    ]

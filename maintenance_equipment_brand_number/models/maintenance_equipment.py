from odoo import fields, models


class MaintenanceEquipment(models.Model):
    _inherit = "maintenance.equipment"

    marca = fields.Char(string="Marca")
    numero = fields.Integer(
        string="Número",
        required=True,
        copy=False,
        default=lambda self: self.env["ir.sequence"].next_by_code(
            "maintenance.equipment.numero"
        ),
    )

    _sql_constraints = [
        ("numero_unique", "unique(numero)", "El número debe ser único."),
    ]

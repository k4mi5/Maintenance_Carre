from . import models

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    seq = env["ir.sequence"]
    equipments = env["maintenance.equipment"].search([("numero", "=", False)])
    for equipment in equipments:
        equipment.numero = seq.next_by_code("maintenance.equipment.numero")

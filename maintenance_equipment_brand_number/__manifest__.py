{
    "name": "Maintenance Equipment Brand and Number",
    "version": "16.0.1.0.0",
    "summary": "Adds brand and unique number to maintenance equipment",
    "author": "",
    "license": "LGPL-3",
    "depends": ["maintenance"],
    "data": [
        "data/ir_sequence.xml",
        "views/maintenance_equipment_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": False,
}

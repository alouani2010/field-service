# Copyright (C) 2018 Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Field Service",
    "summary": "Manage Field Service Locations, Workers and Orders",
    "version": "14.0.1.29.0",
    "license": "AGPL-3",
    "category": "Field Service",
    "author": "Open Source Integrators, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/field-service",
    "depends": ["base_territory", "base_geolocalize", "resource", "contacts"],
    "data": [
        "data/ir_sequence.xml",
        "data/mail_message_subtype.xml",
        "data/module_category.xml",
        "data/fsm_stage.xml",
        "data/fsm_team.xml",
        "security/res_groups.xml",
        "security/ir.model.access.csv",
        "security/ir_rule.xml",
        "report/fsm_order_report_template.xml",
        "views/res_config_settings.xml",
        "views/res_territory.xml",
        "views/fsm_stage.xml",
        "views/fsm_tag.xml",
        "views/res_partner.xml",
        "views/fsm_location.xml",
        "views/fsm_location_person.xml",
        "views/fsm_person.xml",
        "views/fsm_order.xml",
        "views/fsm_order_type.xml",
        "views/fsm_category.xml",
        "views/fsm_equipment.xml",
        "views/fsm_template.xml",
        "views/fsm_team.xml",
        "views/fsm_order_type.xml",
        "views/menu.xml",
        "wizard/fsm_wizard.xml",
    ],
    "demo": [
        "demo/fsm_demo.xml",
        "demo/fsm_equipment.xml",
        "demo/fsm_location.xml",
        "demo/fsm_person.xml",
    ],
    "application": True,
    "development_status": "Production/Stable",
    "maintainers": ["wolfhall", "max3903"],
}

# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Leveesuspens(models.Model):
    _name = 'mudci.leveesuspens'
    _description = 'La table des levées de suspensions'

    susp_id = fields.Many2one(string=_("Suspension"), comodel_name='mudci.suspensions', required=True)
    lesu_observation = fields.Char(string=_("Observation"))
    lesu_documentation = fields.Binary(string=_("Pièce justificative"), attachment=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Lévée de suspension"
            if record.id:
                record.display_name = f"Lévée suspension - {record.id}"

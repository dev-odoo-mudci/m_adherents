# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Resiliations(models.Model):
    _name = 'mudci.resiliations'
    _description = 'La table des résiliations de contrats'

    cont_id = fields.Many2one(string=_('Contrat'), comodel_name='mudci.contrats', required=True)
    resi_motif = fields.Char(string=_('Motif'), required=True)
    resi_dateresiliat = fields.Date(string=_('Date de résiliation'), required=True)
    resi_documentation = fields.Binary(string=_('Pièce justificative'), attachment=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Résiliation"
            if record.id:
                record.display_name = f"Résiliation - {record.id}"
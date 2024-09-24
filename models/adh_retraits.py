# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Retraits(models.Model):
    _name = 'mudci.retraits'
    _description = 'La table des retraits d\'ayants droit'

    bene_id = fields.Many2one(string=_('Bénéficiaire'), comodel_name='mudci.beneficiaires', required=True)
    retr_motif = fields.Char(string=_('Motif'), required=True)
    retr_dateretrait = fields.Date(string=_('Date de rétrait'), required=True)
    retr_documentation = fields.Binary(string=_('Pièce justificative'), attachment=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Bénéficiaire"
            if record.id:
                record.display_name = record.bene_id.bene_nomprenoms
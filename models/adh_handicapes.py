# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Handicapes(models.Model):
    _name = 'mudci.handicapes'
    _description = 'La table des ayants droit handicapés scolarisés'

    # hand_id = fields.Integer(string=_("ID de l'ayant droit handicapé"), required=True, readonly=True)
    bene_id = fields.Many2one(string=_("Bénéficiaire"), comodel_name='mudci.beneficiaires', required=True)
    hand_activation = fields.Selection([('oui', 'Oui'),('non', 'Non')], string=_("Activation"), default='oui', required=True)


    def _compute_display_name(self):
        for record in self:
            record.display_name = "Ayants droit handicapés"
            if record.id:
                record.display_name = record.bene_id.bene_nomprenoms

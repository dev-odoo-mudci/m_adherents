# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Scolarises(models.Model):
    _name = 'mudci.scolarises'
    _description = "La table des ayants droit enfants majeurs scolarisés"

    # scol_id = fields.Integer(string=_("ID de la scolarité"), required=True, readonly=True)
    bene_id = fields.Many2one(string=_('Bénéficiaire'), comodel_name='mudci.beneficiaires', required=True)
    scol_datedebut = fields.Date(string=_('Date de début'), required=True)
    scol_datefin = fields.Date(string=_('Date de fin'), required=True)
    scol_activation = fields.Selection([('oui', 'Oui'),('non', 'Non')], string=_('Activation'), default='oui', required=True)
    scol_activation = fields.Boolean(string=_('Activation'), default=True, required=True,)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Ayants droit scolarisés"
            if record.id:
                record.display_name = record.bene_id.bene_nomprenoms
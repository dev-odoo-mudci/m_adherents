# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Suspensions(models.Model):
    _name = 'mudci.suspensions'
    _description = 'La table de suspensions des bénéficiaires'

    cont_id = fields.Many2one(string=_("Contrat"), comodel_name='mudci.contrats', required=True)
    bene_id = fields.Many2one('mudci.beneficiaires', string=_("Bénéficiaire"), required=True)
    susp_motif = fields.Char(string=_("Motif"), required=True)
    susp_debut = fields.Date(string=_("Date de début"), required=True)
    susp_fin = fields.Date(string=_("Date de fin"), required=True)
    susp_statut = fields.Selection([('encours', 'EN COURS'),('levee', 'LEVEE')], string=_("Statut"), default='encours', required=True)
    susp_documentation = fields.Binary(string=_("Pièce justificative"), attachment=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Bénéficiaire"
            if record.id:
                record.display_name = record.bene_id.bene_nomprenoms
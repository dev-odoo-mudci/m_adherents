# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Contrats(models.Model):
    _name = 'mudci.contrats'
    _description = 'La table des contrats'

    # name = fields.Char('Name')
    bene_id = fields.Many2one(string=_('Bénéficiaire'), comodel_name='mudci.beneficiaires', required=True)
    poli_code = fields.Many2one(string=_('Code police'), comodel_name='mudci.polices', required=True)
    cont_montant = fields.Float(string=_('Montant'), required=True)
    cont_surprime = fields.Float(string=_('Surprime'), default=0)
    cont_ristourne = fields.Float(string=_('Ristourne'), default=0)
    cont_datedebut = fields.Date(string=_('Date de début'), required=True)
    cont_datefin = fields.Date(string=_('Date de fin'))
    cont_resiliation = fields.Date(string=_('Date de résiliation'))
    cont_periodicite = fields.Selection([('mensuelle', 'Mensuelle'), ('trimestrielle', 'Trimestrielle'), ('semestrielle', 'Semestrielle'), ('annuelle', 'Annuelle')], string=_('Périodicité'), required=True)
    cont_delaicarence = fields.Integer(string=_('Délai de carence'), required=True)
    cont_retardpaye = fields.Float(string=_('Retard de paiement'), required=True)
    cont_activation = fields.Selection([('oui', 'Oui'),('non', 'Non')], string=_('Activation'), default='oui', required=True)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Contrat"
            if record.id:
                record.display_name = f"Contrat - {record.id}"
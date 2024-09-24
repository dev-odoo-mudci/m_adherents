# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Polices(models.Model):
    _name = 'mudci.polices'
    _description = 'La table des polices'

    name = fields.Char('Name')
    poli_code = fields.Char(string=_('Code'), required=True)
    poli_standing = fields.Integer(string=_('Standing'), required=True)
    poli_libelle = fields.Char(string=_('Libellé'), required=True)
    poli_appdroitadh = fields.Selection([('adherent', 'Adhérent'),('assure', 'Assuré')], string=_('Applicabilité droit adhérent'), required=True)
    poli_droitadhesion = fields.Float(string=_('Droit adhésion'), required=True)
    poli_periodicite = fields.Selection([('mensuelle', 'Mensuelle'),('trimestrielle', 'Trimestrielle'),('semestrielle', 'Semestrielle'),('annuelle', 'Annuelle')], string=_('Périodicité'), required=True)
    poli_retardpaye = fields.Float(string=_('Retard de payement'), required=True)
    poli_montant = fields.Float(string=_('Montant'), required=True)
    poli_delaicarence = fields.Integer(string=_('Délai de carence'), required=True)
    poli_plafondind = fields.Float(string=_('Plafond/Individu'), required=True)
    poli_plafondfam = fields.Float(string=_('Plafond/famille'), required=True)
    poli_tauxrembpublic = fields.Integer(string=_('Taux de remboursement au public'), required=True)
    poli_tauxrembprive = fields.Integer(string=_('Taux de remboursement au privé'), required=True)
    poli_agelimiteadh = fields.Integer(string=_('Âge limite adhérent'), required=True)
    poli_agelimiteconj = fields.Integer(string=_('Âge limite conjoint'), required=True)
    poli_nbreconjoint = fields.Integer(string=_('Nombre de conjoint'), required=True)
    poli_montantsupconj = fields.Float(string=_('Montant supplémentaire conjoint'), required=True)
    poli_agelimiteenf = fields.Integer(string=_('Âge limite enfant'), required=True)
    poli_agemajorite = fields.Integer(string=_('Âge de la majorité'), required=True)
    poli_nbreenfants = fields.Integer(string=_('Nombre d\'enfants'), required=True)
    poli_montantsupenf = fields.Float(string=_('Montant supplémentaire enfant'), required=True)
    # poli_enfantinvalide = fields.Selection([('oui', 'Oui'),('non', 'Non')], string=_('Enfant invalide'), required=True)
    poli_enfantinvalide = fields.Boolean(string=_('Enfant invalide'), default=True, required=True,)
    poli_nbremaxprescript = fields.Integer(string=_('Nombre maximum de prescriptions'), required=True)
    poli_plafondprescript = fields.Float(string=_('Plafond prescription'), required=True)
    poli_forfaitaccouch = fields.Float(string=_('Forfait accouchement'), required=True)
    poli_tauxprive = fields.Integer(string=_('Taux privé'), required=True)
    poli_tauxpublic = fields.Integer(string=_('Taux public'), required=True)
    poli_seuilalerte = fields.Integer(string=_('Seuil d\'alerte'), required=True)
    poli_activation = fields.Boolean(string=_('Activation'), default=True, required=True,)
    # poli_activation = fields.Selection([('oui', 'Oui'),('non', 'Non')], string=_('Activation'), default='oui', required=True)


    def _compute_display_name(self):
        for record in self:
            record.display_name = "Police"
            if record.poli_code:
                record.display_name = f"Police-{record.poli_code}"
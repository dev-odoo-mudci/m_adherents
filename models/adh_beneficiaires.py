# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Beneficiaires(models.Model):
    _name = 'mudci.beneficiaires'
    _description = 'La table des bénéficiaires'

    # name = fields.Char('Name')
    loca_id = fields.Many2one(string=_('Localité'), comodel_name='mudci.localites',)
    bene_matricule = fields.Char(string=_('Matricule'), default='ENMXX7D85SWF4SDC', required=True,)
    bene_codeid = fields.Char(string=_('Code ID'), default='ENMXX7D85SWF4SDC', required=True,)
    bene_dateadhesion = fields.Date(string=_('Date adhésion'), default=fields.Date.context_today,)
    bene_statut = fields.Selection(string=_('Statut'), selection=[('adherent', 'Adherent'),('conjoint', 'Conjoint'),('enfant', 'Enfant'),], required=True,)
    bene_idadherent = fields.Char(string=_('ID adhésion'), default='ENMXX7D85SWF4SDC', required=True,)
    bene_nom = fields.Char(string=_('Nom'), required=True, size=30,)
    bene_prenoms = fields.Char(string=_('Prénoms'), required=True, size=30)
    bene_nomprenoms = fields.Char(string=_('Nom & Prénoms'), compute='_compute_bene_nomprenoms', store=False)
    bene_datenaissance = fields.Date(string=_('Date de naissance'), default=fields.Date.context_today, required=True,)
    bene_genre = fields.Selection(string=_('Genre'), selection=[('masculin', 'Masculin'), ('feminin', 'Feminin')], required=True,)
    bene_lieunaissance = fields.Char(string=_('Lieu de naissance'), required=True, size=80)
    bene_perscontact = fields.Char(string=_('Personne contact'), default='', size=60)
    bene_adresse = fields.Char(string=_('Adresse'), default='', size=100)
    bene_mobile1 = fields.Char(string=_('Mobile 1'), default='', size=20)
    bene_mobile2 = fields.Char(string=_('Mobile 2'), default='', size=20)
    bene_email = fields.Char(string=_('Email'), default='', size=60)
    bene_boitepostal = fields.Char(string=_('Boite postal'), default='', size=30)
    # bene_activation = fields.Selection(string=_('Activation'), selection=[('oui', 'Oui'),('non', 'Non'),], required=True, default='oui',)
    # bene_suspension = fields.Selection(string=_('Suspension'), selection=[('oui', 'Oui'),('non', 'Non'),], required=True, default='non',)
    bene_activation = fields.Boolean(string=_('Activation'), default=True, required=True,)
    bene_suspension = fields.Boolean(string=_('Suspension'), default=True, required=False,)

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Bénéficiaire"
            if record.bene_nom and record.bene_prenoms:
                record.display_name = f"{record.bene_nom} {record.bene_prenoms}"


    @api.depends('bene_nom', 'bene_prenoms')
    def _compute_bene_nomprenoms(self):
        for record in self:
            record.bene_nomprenoms = f"{record.bene_nom} {record.bene_prenoms}" if record.bene_nom and record.bene_prenoms else ''
# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class Localites(models.Model):
    _name = 'mudci.localites'
    _description = 'La table des localités'

    # name = fields.Char('Name')
    loca_nom = fields.Char(string=_('Nom localité'), required=True,) #size=40
    loca_activation = fields.Selection(string=_('Activation'), selection=[('oui', 'Oui'),('non', 'Non'),], required=True, default='oui',)

    # _sql_constraints = [
    #     ('nom_length_check', 'CHECK(char_length(nom) <= 40)', 'Le nom de la localité ne peut pas dépasser 40 caractères.'),
    #     ('unique_nom', 'UNIQUE(LOWER(nom))', 'Cette localité existe déjà dans la base de donnée !')
    # ]

    def _compute_display_name(self):
        for record in self:
            record.display_name = "Localité"
            if record.loca_nom:
                record.display_name = record.loca_nom


    @api.constrains('loca_nom')
    def _check_loca_nom(self):
        for record in self:
            if len(record.loca_nom) < 3 or len(record.loca_nom) > 40:
                raise ValidationError(_("Le nom de la localité doit contenir entre 3 et 40 caractères."))
            # Rechercher une localité avec le même nom (insensible à la casse)
            domain = [('id', '!=', record.id), ('loca_nom', '=ilike', record.loca_nom)]
            # localite = self.search(domain, limit=1)
            localite = self.search_count(domain)
            if localite:
                raise ValidationError(_(f'Cette localité "{record.loca_nom}" existe déjà dans la base de donnée !'))
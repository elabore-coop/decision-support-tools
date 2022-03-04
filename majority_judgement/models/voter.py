# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class MajorityJudgementVoter(models.Model):
    _name = "voter"
    _description = "Majority Judgement voter"

    partner_id = fields.Many2one(
        "res.partner", string=_("Associated contact"), required=True
    )
    vote_id = fields.Many2one("vote", string=_("Vote"))
    has_voted = fields.Boolean(string="Has voted")
    vote_timestamp = fields.Datetime(string=_("Has voted on"))

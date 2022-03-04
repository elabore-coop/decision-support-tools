# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MajorityJudgementCandidate(models.Model):
    _name = "candidate"
    _description = "Majority Judgement candidate"

    name = fields.Char(string=_("Name"), required=True)
    description = fields.Text(string=_("Description"))
    vote_id = fields.Many2one("vote", string=_("Vote"))
    final_grade = fields.Many2one("grade", string=_("Final Grage"))
    ballot_line_ids = fields.One2many(
        "ballot.line", "candidate_id", string=_("Ballot lines")
    )

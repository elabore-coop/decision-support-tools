# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MajorityJudgementBallotLine(models.Model):
    _name = "ballot.line"
    _description = "Majority Judgement ballot line"

    candidate_id = fields.Many2one("candidate", string=_("Candidate"), required=True)
    grade_id = fields.Many2one("grade", string=_("Grade"), required=True)

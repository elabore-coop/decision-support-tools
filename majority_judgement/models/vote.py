# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class MajorityJudgementVote(models.Model):
    _name = "vote"
    _description = "Majority Judgement vote"

    name = fields.Char(string=_("Name"), required=True)
    description = fields.Text(string=_("Description"))
    question = fields.Char(string=_("Question"), required=True)
    start_time = fields.Datetime(string=_("Start time"))
    end_time = fields.Datetime(string=_("End time"))

    grade_ids = fields.One2many("grade", "vote_id", string=_("Grades"))
    candidate_ids = fields.One2many("candidate", "vote_id", string=_("Candidate"))
    voter_ids = fields.One2many("voter", "vote_id", string=_("Voters"))

    state = fields.Selection(
        [("draft", "Draft"), ("opened", "Opened"), ("closed", "Closed")],
        string=_("Status"),
        index=True,
        readonly=True,
        default="draft",
        track_visibility="onchange",
        copy=False,
    )

    @api.model
    def create(self, values):
        record = super(MajorityJudgementVote, self).create(values)
        record.generate_default_grades()
        return record

    def generate_default_grades(self):
        for grade in self.grade_ids:
            grade.unlink()
        grade_models = self.env["grade.model"].search([])
        for model in grade_models:
            vals = {
                "name": model.name,
                "color": model.color,
                "sequence": model.sequence,
                "vote_id": self.id,
            }
            self.env["grade"].create(vals)

    def action_open_vote(self):
        self.state = "opened"

    def action_close_vote(self):
        self.state = "closed"

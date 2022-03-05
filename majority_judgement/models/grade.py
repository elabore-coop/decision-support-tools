# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class MajorityJudgementGradeModel(models.Model):
    _name = "grade.model"
    _description = "Majority Judgement grade model"

    name = fields.Char(string=_("Name"), required=True)
    color = fields.Integer("Color Index", default=0)
    sequence = fields.Integer()


class MajorityJudgementGrade(models.Model):
    _name = "grade"
    _description = "Majority Judgement grade"

    name = fields.Char(string=_("Name"), required=True)
    color = fields.Integer("Color Index", default=0)
    sequence = fields.Integer()
    vote_id = fields.Many2one("vote", string=_("Vote"))

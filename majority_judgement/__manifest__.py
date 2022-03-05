# © 2022 Elabore
# @author Stéphan Sainléger <stephan.sainleger@elabore.coop>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Majority Judgement",
    "summary": "Majority Judgement addons to support democracy in your organisation",
    "version": "12.0.0.0.1",
    "category": "Generic Modules/Others",
    "license": "AGPL-3",
    "author": "Elabore",
    "website": "https://elabore.coop/",
    "installable": True,
    "auto_install": False,
    "application": True,
    "description": """
==================
Majority Judgement
==================
This module provides majority judgement fonctionnalities.

Installation
============
Just install majority_judgement, all dependencies will be installed by default.

Known issues / Roadmap
======================

Bug Tracker
===========
Bugs are tracked on `GitHub Issues
<https://github.com/elabore-coop/decision-support-tools/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smashing it by providing a detailed and welcomed feedback.

Credits
=======

Images
------
* Elabore: `Icon <https://elabore.coop/web/image/res.company/1/logo?unique=f3db262>`_.

Contributors
------------
* Stéphan Sainléger <https://github.com/stephansainleger>

Funders
-------
The development of this module has been financially supported by:
* Elabore (https://elabore.coop)

Maintainer
----------
This module is maintained by ELABORE.

""",
    "depends": ["base"],
    "external_dependencies": {
        "python": [],
    },
    "data": [
        "views/vote.xml",
        "views/candidate.xml",
        "views/grade_model.xml",
        "views/menus.xml",
        "security/ir.model.access.csv",
    ],
    "demo": [],
    "js": [],
    "css": [],
    "qweb": [],
}

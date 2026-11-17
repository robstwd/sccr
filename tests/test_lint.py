"""Tests for the LinkML naming convention."""

from pathlib import Path

import yaml
from linkml.linter.linter import Linter
from linkml.linter.rules import StandardNamingRule
from linkml_runtime import SchemaView

from sccr_poc.datamodel import MAIN_SCHEMA_PATH


def test_enum_naming_convention():
    config_path = Path(__file__).parent.parent / ".linkmllint.yaml"
    with config_path.open(encoding="utf-8") as config_file:
        linter = Linter(yaml.safe_load(config_file))
    rule = StandardNamingRule(linter.config.rules.standard_naming)
    schema = SchemaView(str(MAIN_SCHEMA_PATH))

    assert not list(rule.check(schema))

    values = schema.get_enum("PersonStatus").permissible_values
    values["alive"] = values.pop("ALIVE")
    problems = list(rule.check(schema))
    assert any("has name 'alive'" in problem.message for problem in problems)

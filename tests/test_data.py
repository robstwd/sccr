"""Data test."""

import os
import glob
import pytest
from pathlib import Path

import sccr_poc.datamodel.sccr_poc
from linkml_runtime.loaders import yaml_loader
from sccr_poc.datamodel import MAIN_SCHEMA_PATH

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, "*.yaml"))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, "*.yaml"))


def test_main_schema_exists():
    assert MAIN_SCHEMA_PATH.is_file()


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(
        sccr_poc.datamodel.sccr_poc,
        target_class_name,
    )
    obj = yaml_loader.load(filepath, target_class=tgt_class)
    assert obj

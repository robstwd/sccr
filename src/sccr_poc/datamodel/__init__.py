"""Data model package for sccr."""

from pathlib import Path
from .sccr_poc import *  # noqa: F403

THIS_PATH = Path(__file__).parent

SCHEMA_DIRECTORY = THIS_PATH.parent / "schema"
MAIN_SCHEMA_PATH = SCHEMA_DIRECTORY / "sccr_poc.yaml"

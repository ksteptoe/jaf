"""
To install run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command $(package) inside your current environment.
"""

import logging
import click
from ResearchFrame import ResearchFrame
from pathlib import Path
import yaml

__author__ = "Kevin Steptoe"
__copyright__ = "Kevin Steptoe"
__license__ = "MIT"

from jaf import __version__

_logger = logging.getLogger(__name__)


@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.version_option(version=__version__, prog_name="insight")
def cli(input: str) -> None:
    """
    Analyze Excel sheets from MailChimp and insightly sources.

    Args:
        input: Input Excel files to analyze.

    """
    config = Path("template.yml")
    with open(config, 'r') as file:
        email_templates = yaml.safe_load(file)
    rf = ResearchFrame(email_templates, input)
    print(rf)


if __name__ == "__main__":

    cli()

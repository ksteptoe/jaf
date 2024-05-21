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
@click.command()
@click.argument('input', type=click.Path(exists=True), help="Input file path (must exist).")
@click.argument('output', type=click.Path(), required=False, default='output.xlsx',
                help="Output file path (defaults to 'output.xlsx' if not provided).")
@click.option('-t', '--template', type=click.Path(), default='template.yml',
              help='Template file path (defaults to "template.yml").')
@click.version_option(version=__version__, prog_name="insight")
def cli(input: str, output: str, template: str) -> None:
    """
    Analyze Excel sheets from MailChimp and insightly sources.

    Args:
        input: Input Excel files to analyze.

    """
    config = Path("template.yml")
    with open(config, 'r') as file:
        email_templates = yaml.safe_load(file)
    rf = ResearchFrame(email_templates, input)


if __name__ == "__main__":

    cli()

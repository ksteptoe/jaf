"""
To install run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command $(package) inside your current environment.
"""

import logging
import click
from jaf.ResearchFrame import ResearchFrame
from pathlib import Path
import yaml

__author__ = "Kevin Steptoe"
__copyright__ = "Kevin Steptoe"
__license__ = "MIT"

from jaf import __version__

_logger = logging.getLogger(__name__)


@click.command()
@click.argument('input', type=click.Path(exists=True), required=True)
@click.argument('output', type=click.Path(), required=False, default='output.xlsx')
@click.option('-t', '--email_template_file', type=click.Path(), default='template.yml',
              help='Email template file path (defaults to "template.yml").')
@click.option('-s', '--sheet_name', default='Sheet1',
              help='Sheet name in the input Excel file (defaults to "Sheet1").')
@click.version_option(version=__version__, prog_name="insight")
def cli(input: str, output: str, email_template_file: str, sheet_name: str) -> None:
    """
    Analyze Excel sheets from MailChimp and insightly sources.

    Args:
        input: Input Excel files to analyze.
        output ( optional ): Output file path.
        email_template_file: Email templates file path.
        sheet_name : Sheet name in the input Excel file (defaults to "Sheet1")

    """
    # Validate input and output file extensions
    validate_file_extension(input, '.xlsx')
    validate_file_extension(output, '.xlsx')

    # Validate email template file extension
    validate_file_extension(email_template_file, '.yml')

    config = Path(email_template_file)
    with open(config, 'r') as file:
        templates = yaml.safe_load(file)
    rf = ResearchFrame(input, output, templates, sheet_name)
    rf.output_xl()


def validate_file_extension(file_path, expected_extension):
    """
    Validate file extension.

    Args:
        file_path: Path to the file.
        expected_extension: Expected file extension (with leading dot).
    """
    if not file_path.endswith(expected_extension):
        raise click.BadParameter(f"File '{file_path}' must have extension '{expected_extension}'.")


if __name__ == "__main__":

    cli()

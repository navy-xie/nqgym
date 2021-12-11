import os

import click

from cookiecutter.main import cookiecutter

from . import config
from . import __version__


@click.group()
@click.version_option()
def cli():
    """NQGym is a greate tool to help you generate project templates.
    """
    pass


@cli.command()
def create():
    """Create a Python project.
    """
    # the template path
    template_path = config.PROJECT_TEMPLATE_PATH

    # print the cheer message
    cheer_msg = f"Welcome to NQGym v{__version__}. (Navy Xie @ 2021)"
    click.secho(cheer_msg, fg="green")

    # generate the project
    cookiecutter(str(template_path))

    # print the bye message
    bye_msg = \
        "Generation finished.\n" \
        "  Please find the generated project from the current directory.\n" \
        "  You can contact Navy Xie if you need help, \n" \
        "  or want to buy him a cup of coffee ;-P"
    click.secho(bye_msg, fg="green")

import click

from {{cookiecutter.package_name}}.hello import say_hello


@click.group()
@click.version_option()
def cli():
    """A general CLI for the Python project.
    """
    pass


@cli.command()
@click.option("-n", "--name", default="Peter", show_default=True,
              help="A sample command.")
def hello(name):
    """A sample command.
    """
    say_hello(name)

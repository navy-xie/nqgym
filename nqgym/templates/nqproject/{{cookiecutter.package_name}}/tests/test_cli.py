import {{cookiecutter.package_name}}

from {{cookiecutter.package_name}}.cli import cli


def test_version(runner):
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert {{cookiecutter.package_name}}.__version__ in result.output

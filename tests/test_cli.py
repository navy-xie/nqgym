import nqgym

from nqgym.cli import cli


def test_version(runner):
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert nqgym.__version__ in result.output

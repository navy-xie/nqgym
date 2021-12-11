# Contributing

## Setting up for local development

### Requirements

- We use `conda` to manage the Python environment. Please follow [the guide][1] to install `conda`.
- We use `make` to mange build jobs. If you are on Windows, please follow [the guide][2] to install `make`.

### Create an environment

    $ make env
    $ conda activate nqgym

### Install the package and other dependencies

    $ make install

## Testing

    $ make codestyle
    $ make test
    $ make coverage

## Release

    $ make release


[1]: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html "Conda Installation"
[2]: https://gist.github.com/evanwill/0207876c3243bbb6863e65ec5dc3f058#make "Install make to git-bash on Windows"

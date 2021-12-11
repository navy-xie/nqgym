# NQGym

A command-line utility that creates Python projects.

## Features

`NQGym` can help you create a Python project template, or a web service project template.

Features of the Python project template:

- Use `make` to facilitate the development process, such as 
    - creating virtual environment
    - installing dependent libs
    - building the dist
    - testing and running UT coverage
- Support `CLI` (Command-Line Interface) to start / stop the app or run other commands from the Python entry point.

## How to use it

Install from PyPi:

```bash
$ pip install -U nqgym
```

Find the help:

```bash
$ nqgym --help
$ nqgym create --help
```

Create a Python project:

```bash
$ nqgym create
```

The generator will ask you for some input data, you might want to have at hand before generating the project.  
The input variables, with their default values (some auto generated) are:

- `project_name`: The name of the project.
- `package_name`: The name of the Python package. By default, based on the project name.
- `python_version`: The version of Python you want to use.

## More details

After using the generator, your new project (the directory created) will contain an extensive `README.md` with instructions for development, deployment, etc. You can read it to find more details.


## How to contribute

Please follow the guide [contribution](./CONTRIBUTING.md) to develop and contribute NQGym.

## Release notes

### v1.0.0 12/8/2021

- Project init.
- Created the Python project template.
- Support make, cli.
- Support UT and UT coverage.

## License

This project is licensed under the terms of the BSD license.

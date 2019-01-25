# Sass4Dash
Example with SASS compiler and watcher for [dash by plotly](https://plot.ly/products/dash) project

## Index

- [Overview](#overview)
- [Requirements](#requirements)
- [Dependences](#dependences)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Development](#development)
- [Project folder structure](#project-folder-structure)

## Overview

The project shows how to manage SASS in a Dash project. With two python scripts included you can watch for SASS code changes and compile to CSS.

## Requirements

- Python 2.7 or Python 3.5 (or above)
- virtualenv (optional)

Python 3.7 is used by default

## Dependences

For this develop utility three principal dependences are used:
- [Dash by plotly](https://plot.ly/products/dash): To code awesome graphs
- [Libsass-python](https://github.com/sass/libsass-python): To compile SASS files
- [Watchdog](https://github.com/gorakhargosh/watchdog): To watch code files changes

## Getting Started

- Create a virtualenv and activate it

```
virtualenv -p python3.7 venv
source venv/bin/activate
```

- Install requirements

```
pip install -r requirements.txt
```
or is you are developing new features
```
pip install -r requirements-dev.txt
```
- Generate custom styles (compile SASS files - requirements-dev are needed in this step)

```
python scripts/compile_styles.py
```
Previously yoy have to create folder ``/src/assets/css``
- Run App

```
python src/app.py
```

- Now you can open `http://localhost:8050`


  \* These options can be changed with ``.env`` file (for example ``APP_PORT=8051``)

## Configuration

There is a environment file example with all the possible configs variables.
Copy or create an environment file at the root of the project with your preferences.

Environment variables present are:

| Variables                | Description                                                                            |
| ------------------------ | -------------------------------------------------------------------------------------- |
| APP_HOST                 | Host to serve dashboards                                                               |
| APP_PORT                 | Port to serve dashboards                                                               |
| DEBUG                    | Debug mode (True or False) for development server                                      |

## Development

- Yoy can develop with auto-compile SASS files changes with
```
$ python scripts/watch_styles.py
```

## Project folder structure

```
scripts/          # SASS management scripts
src/              # Source code
|--
```

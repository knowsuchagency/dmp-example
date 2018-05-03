#!/usr/bin/env python

import sys; sys.path.append('run_py_vendor')
from shell_utils import shell

import click

@click.group()
def main():
    """The main command."""


@main.command()
def docker_run():
    """Run in docker."""
    shell(
        f'docker run -p 8000:8000 -v "$PWD"/mysite:/mysite/ -it --rm dmp bash'
    )

if __name__ == '__main__':
    main()
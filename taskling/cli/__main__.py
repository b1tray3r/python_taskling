"""
Entrypoint for the app.
"""
import logging

import click
from rich.logging import RichHandler

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(
    name='taskling',
    context_settings=CONTEXT_SETTINGS,
    commands=[
    ]
)
@click.version_option(None, '--version', '-v')
@click.option(
    '--log-level',
    default='INFO',
    show_default=True,
    type=click.Choice(
        ['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        case_sensitive=False
    )
)
def main(log_level):
    console_fmt = '%(message)s'
    datefmt = '%Y-%m-%d %H:%M:%S'

    handler = RichHandler()
    handler.setFormatter(logging.Formatter(console_fmt, datefmt))

    logger = logging.getLogger('devenv')
    logger.addHandler(handler)
    choices = {'DEBUG': 10, 'INFO': 20, 'WARNING': 30, 'ERROR': 40}
    logger.setLevel(choices.get(log_level, 40))


if __name__ == '__main__':
    main()

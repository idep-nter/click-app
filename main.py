import click

from commands import stat, read


@click.group(help="CLI application which retrieves and prints data from the backend")
def cli():
    pass


cli.add_command(stat.stat)
cli.add_command(read.read)

if __name__ == "__main__":
    cli()

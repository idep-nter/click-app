import click
import requests


@click.command()
@click.option(
    "--base_url",
    default="http://localhost/",
    help="Set a base URL for a REST server. Default is http://localhost/",
)
@click.option(
    "--output",
    default=None,
    help="Set the file where to store the output. Default is -, i.e. the stdout",
)
@click.argument("uuid", type=int, nargs=1)
def read(base_url, output, uuid):
    url = f"{base_url}file/{uuid}/read/"
    response = requests.get(
        url, headers={"Content-Disposition": "name", "Content-Type": "mimetype"}
    )
    response.raise_for_status()
    if not output:
        return response

    with open(output, "w") as f:
        f.write(response.text)

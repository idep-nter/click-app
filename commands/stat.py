import click
import requests
import json


@click.command()
@click.option(
    "--base_url",
    default="http://localhost/",
    help="Set a base URL for a REST server. Default is http://localhost/",
)
@click.argument("uuid", type=int, nargs=1)
def stat(base_url, uuid):
    url = f"{base_url}file/{uuid}/stat/"
    response = requests.get(url)
    response.raise_for_status()
    json_response = response.json()
    pretty_response = json.dumps(json_response, indent=4)
    print(pretty_response)
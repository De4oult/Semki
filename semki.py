from functions import initialize, download

import click

@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)

@cli.command()
@click.argument('name')
@click.argument('author')
def init(name, author): # init workspace
    initialize(name, author)

@cli.command()
@click.argument('name')
def get(name): # get package from 
    download(name)

if __name__ == '__main__':
    cli(obj={})
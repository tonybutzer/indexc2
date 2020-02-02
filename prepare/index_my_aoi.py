from index_lib import index_records
import click


@click.command()
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--path', '-p', default='', help='WRS2 PATH')
@click.option('--row', '-r', default='', help='WRS2 ROW')
@click.option('--year', '-y', default='', help='YEAR')
@click.argument('product')
def cli(verbose, path, row, year, product):
    """This is an example script to learn Click."""
    if verbose:
        click.echo("We are in the verbose mode.")
    click.echo("Add records to this product: {0}".format(product))
    print(path,row,year,product)


    index_records(path,row,years)



if __name__ == '__main__':
    cli()

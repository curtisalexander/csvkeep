#!/usr/bin/env python

import csv
import click    # pip install click -- assumes version 5.x

@click.command()
@click.option('--incsv', type=click.File(mode='rU', lazy=True), help='input csv')
@click.option('--outcsv', type=click.File(mode='w', lazy=True), help='output csv')
@click.option('--cols', help='comma separated list of columns to keep')

def keep_cols(incsv, outcsv, cols):
    """Filter a CSV file - only keeping specific columns.  Like *nix 'cut' (or SQL 'select') but filters based on named columns.

    \b
    Example:
        csvkeep.py --incsv /dir/to/infile.csv --outcsv /dir/to/outfile.csv --cols var1,var2,var5
    """
    keep = [c.strip() for c in cols.split(',')]
    csv_reader = csv.DictReader(incsv)
    full_header = next(csv_reader)  # get header
    csv_writer = csv.DictWriter(outcsv, list(keep))
    csv_writer.writeheader()
    for row in csv_reader:
        csv_writer.writerows([dict(zip([c for c in list(keep)], [row[c] for c in list(keep)]))])

if __name__ == '__main__':
    keep_cols()

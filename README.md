# csvkeep
Filter a CSV file - only keeping specific columns.  Like \*nix `cut` (or SQL `select`) but filters based on named columns.

## Usage
```
csvkeep.py [OPTIONS]

Options:
  --incsv FILENAME   input csv
  --outcsv FILENAME  output csv
  --cols TEXT        comma separated list of columns to keep
  --help             Show this message and exit.
```

## Example
```
$ csvkeep.py --incsv /dir/to/infile.csv --outcsv /dir/to/outfile.csv --cols var1,var2,var5
```

## Requirements
[click](http://click.pocoo.org) - command line library for Python

```pip install click``` 

## Related
[csvkit](https://github.com/onyxfish/csvkit) - a suite of utilities for converting to and working with CSV

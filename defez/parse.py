""" Generators parsing the samples in various ways: Left to right, up to down etc
"""

import csv

def parse_lrud(sample_path):
    """ Left to right then up to down
    """
    with open(sample_path) as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            for token in row:
                yield token.strip()

def parse_udlr(sample_path):
    """ Up to down then left to right
    """
    with open(sample_path) as file_handler:
        reader = csv.reader(file_handler)
        rows = list(reader)
        row_width = len(rows[0])
        n_rows = len(rows)
        for row_idx in range(n_rows):
            for col_idx in range(row_width):
                yield rows[row_idx][col_idx].strip()

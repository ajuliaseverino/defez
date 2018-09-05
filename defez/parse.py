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
                token = token.strip()
                if token:
                    yield token

def parse_udlr(sample_path):
    """ Up to down then left to right
    """
    with open(sample_path) as file_handler:
        reader = csv.reader(file_handler)
        rows = list(reader)
        row_width = len(rows[0])
        n_rows = len(rows)
        for col_idx in range(row_width):
            for row_idx in range(n_rows):
                token = rows[row_idx][col_idx].strip()
                if token:
                    yield token


def parse_udrl(sample_path):
    """ Up to down then right to left
    """
    with open(sample_path) as file_handler:
        reader = csv.reader(file_handler)
        rows = list(reader)
        row_width = len(rows[0])
        n_rows = len(rows)
        for col_idx in range(row_width):
            for row_idx in list(range(n_rows))[::-1]:
                token = rows[row_idx][col_idx].strip()
                if token:
                    yield token

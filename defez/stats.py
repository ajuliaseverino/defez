""" Module for basic statistical analysis
"""

from collections import defaultdict

def first_order(token_generators):
    """ Computes first order stats, token frequencies

    Args:
      token_generators - list of generators over tokens

    Returns:
      tok_freqs - {tok: norm_freq}
    """
    counts = defaultdict(int)
    total_count = 0
    for token_generator in token_generators:
        for token in token_generator:
            counts[token] += 1
            total_count += 1

    return {tok: count / total_count for tok, count in counts.items()}

def second_order(token_generators):
    """ Computes first order stats, token frequencies

    Args:
      token_generators - list of generators over tokens

    Returns:
      tok_freqs - {tok: norm_freq}
    """
    counts = defaultdict(int)
    total_count = 0
    for token_generator in token_generators:
        last_token = None
        for token in token_generator:
            if last_token is not None:
                counts[(last_token, token)] += 1
                total_count += 1
            last_token = token

    return {tok: count / total_count for tok, count in counts.items()}

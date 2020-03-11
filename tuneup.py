#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "Jonathan Jones"

import cProfile
import pstats
import timeit
from collections import Counter


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def inner_function(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        return_value = func(*args, **kwargs)
        pr.disable()
        sortby = 'cumulative'
        p_stat = pstats.Stats(pr).sort_stats(sortby)
        p_stat.print_stats()
        return return_value
    return inner_function


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    movies.sort()
    return [item for item, count in Counter(movies).items() if count > 1]


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    t = timeit.Timer()
    result = t.repeat(repeat=7, number=3)
    print(
        "Best time across 7 repeats of 3 runs per repeat:",
        min(result))


def main():
    """Computes a list of duplicate movie entries"""
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
    timeit_helper()

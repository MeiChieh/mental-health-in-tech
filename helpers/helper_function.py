import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from termcolor import cprint
import sqlite3
import pycountry_convert as pc
from collections import Counter
from wordcloud import WordCloud
import os


# plotting related
def s():
    """
    lazy function for plt.show()
    """
    plt.show()


def fs(w=3, h=3):
    """
    lazy function for setting figure size

    Args:
        w (int, optional): set fig width. Defaults to 3.
        h (int, optional): set fig length. Defaults to 3.
    """
    plt.figure(figsize=(w, h))


def bprint(input):
    """
    style printing

    Args:
        input (any): content to print
    """
    cprint(f"\n{input}", "cyan", attrs=["bold"])


def round_percent(val, has_percent=False):
    """return float in percentage rounded to 2nd digit

    Args:
        val (_float_): float to round
        has_percent (bool, optional): whether percentage sign should be shown. Defaults to False.

    Returns:
        float/ string: if has_percent, return string (val%), else return int(%)
    """
    result = round(val*100, 2)
    if has_percent:
        return f"{result}%"
    else:
        result


def mark_bar(plot):
    """append bar values on the bars

    Args:
        plot (_type_): plot
    """
    for i in plot.containers:
        plot.bar_label(i,)


# based on UN classification
west_european_countries = [
    'Austria',
    'Belgium',
    'France',
    'Germany',
    'Liechtenstein',
    'Luxembourg',
    'Monaco',
    'Netherlands',
    'Switzerland',
]


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(
        country_alpha2)
    continent_name = pc.convert_continent_code_to_continent_name(
        country_continent_code)
    return continent_name


def get_stopwords_ls():
    """
    read stopwords file and return the list of words for wordcloud

    Returns:
        list: list of words
    """
    # get the absolute path of the file
    file_path = os.path.join(os.path.dirname(__file__), 'stopwords.txt')
    f = open(file_path, 'r')
    stopwords_ls = f.readlines()
    return stopwords_ls


def make_word_cloud(column):
    """
    Wrapper function for wordcould module, used for making 
    an image of the most commonly occured words from a dataframe column.

    Args:
        column (pd.Series): a column in a dataframe
    """
    # join interested column contents into a big string
    text = ' '.join(list(column))
    stopwords_ls = get_stopwords_ls()
    # convert stopwords_ls into set for the WordCloud class
    stopwords_set = {i.strip() for i in stopwords_ls}
    # Generate a word cloud image
    wordcloud = WordCloud(stopwords=stopwords_set).generate(text)
    plt.imshow(wordcloud, cmap='plasma')
    plt.axis("off")
    s()

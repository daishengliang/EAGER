#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
This script use Latent Dirichlet Allocation (LDA) with Gibbs sampling to generate topics for tweets.

Command line: python tweet_lda.py -if input_filename 

Arguments:

    -if|--input_file|str|required, default: None||the input file
"""

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import pandas as pd
import sys
import argparse
import preprocessor as p # pip install tweet-preprocessor


def parse_args():
    """Parse the arguments.
    Parse the command line arguments/options using the argparse module
    and return the parsed arguments (as an argparse.Namespace object,
    as returned by argparse.parse_args()).
    Returns:
        argparse.Namespace: the parsed arguments
    """

    # Parse command line options/arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-if', '--input_file', required=True)

    # parser.add_argument('-of', '--output_file', required=True)

    args = parser.parse_args()

    return args


def main(argv=None):
    """This is the main function.
    """
    args = parse_args()
    tokenizer = RegexpTokenizer(r'\w+')

    # create English stop words list
    en_stop = get_stop_words('en')

    # Create p_stemmer of class PorterStemmer
    p_stemmer = PorterStemmer()
        
    tweets = pd.read_csv(args.input_file)
    doc_set =[]
    for i in tweets.text:
        doc_set.append(p.clean(i))

    # list for tokenized documents in loop

    texts = []

    # loop through document list
    for i in doc_set:
        
        # clean and tokenize document string
        raw = i.lower()
        tokens = tokenizer.tokenize(raw)

        # remove stop words from tokens
        stopped_tokens = [i for i in tokens if not i in en_stop]
        
        # stem tokens
        stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
        
        # add tokens to list
        texts.append(stemmed_tokens)

    # turn our tokenized documents into a id <-> term dictionary
    dictionary = corpora.Dictionary(texts)
        
    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary, passes=20)
    print(ldamodel.print_topics())

if __name__=="__main__":
    sys.exit(main())

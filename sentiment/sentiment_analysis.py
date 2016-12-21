#!/usr/bin/env python3


# -*- coding: utf-8 -*-
"""
This script predicts the sentiment for tweets.

Command line: python sentiment_analysis.py -train training_data -if input_filename -of "results/filename.csv"

Arguments:

    -train|--training_data|str|required||User provided training data
    -if|--input_file|str|required, default: None||the input file
    -of|--output_file|str|required, default: None||the output file for sentiment analysis
"""
import pandas as pd
import sys
import argparse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer


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
    parser.add_argument('-train', '--training_data', required=True,
                        help='Please provide training data')

    parser.add_argument('-if', '--input_file', required=True)
    parser.add_argument('-of', '--output_file', required=True)


    args = parser.parse_args()

    return args


def split_into_lemmas(tweet):
        bigram_vectorizer = CountVectorizer(ngram_range=(1, 3), token_pattern=r'\b\w+\b', min_df=1)
        analyze = bigram_vectorizer.build_analyzer()
        return analyze(tweet)

def main(argv=None):
    """This is the main function.
    """
    args = parse_args()
    tweets = pd.read_csv(args.input_file)
    tweets = tweets[800:]
    f = pd.read_csv(args.training_data, sep=',', names=['Text', 'Sentiment'], dtype=str, header=0)
    f = f[:800]

    

    bow_transformer = CountVectorizer(analyzer=split_into_lemmas, stop_words='english', strip_accents='ascii').fit(f['Text'])

    text_bow = bow_transformer.transform(f['Text'])
    tfidf_transformer = TfidfTransformer().fit(text_bow)
    tfidf = tfidf_transformer.transform(text_bow)

    text_tfidf = tfidf_transformer.transform(text_bow)

    classifier_nb = MultinomialNB().fit(text_tfidf, f['Sentiment'])

    sentiments = pd.DataFrame(columns=['text', 'class', 'prob'])
    i = 0
    for _, tweet in tweets.iterrows():
        i += 1
        try:
            bow_tweet = bow_transformer.transform(tweet)
            tfidf_tweet = tfidf_transformer.transform(bow_tweet)
            sentiments.loc[i-1, 'text'] = tweet.values[0]
            sentiments.loc[i-1, 'class'] = classifier_nb.predict(tfidf_tweet)[0]
            sentiments.loc[i-1, 'prob'] = classifier_nb.predict_proba(tfidf_tweet)[0][1]
        except Exception as e:
            sentiments.loc[i-1, 'text'] = tweet.values[0]

    sentiments.to_csv(args.output_file, encoding='utf-8')
    print (sentiments)

if __name__=="__main__":
    sys.exit(main())
#!/usr/bin/python
# pylint: disable=line-too-long

'''Main module of SINE practice about BM25 ranking of tweets'''

import sys
import os
import getopt
import csv
import math
import numpy
from inc.query import Query
from inc.tweets import Tweets
from inc.frecuencies import Frecuencies


def process_arguments(argv):
    '''Process script arguments and check if there an error'''

    help_text = 'Help here'
    local_tweet_file = ''
    local_queries_file = ''
    local_frecuencies_file = ''
    local_entity = ''
    local_destination_dir = 'result'
    local_b = ''
    local_k1 = ''
    local_k2 = ''
    try:
        opts, _ = getopt.getopt(argv, "ht:q:f:d:e:",
                                ["tweetFile=", "queriesFile=", "frecuenciesFile=", "destinationDir=", "entity=", "k1=", "k2=", "b="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-t", "--tweetFile"):
            local_tweet_file = arg
        elif opt in ("-q", "--queriesFile"):
            local_queries_file = arg
        elif opt in ("-f", "--frecuenciesFile"):
            local_frecuencies_file = arg
        elif opt in ("-d", "--destinationDir"):
            local_destination_dir = arg
        elif opt in ("-e", "--entity"):
            local_entity = arg
        elif opt == "--b":
            local_b = float(arg)
        elif opt == "--k1":
            local_k1 = float(arg)
        elif opt == "--k2":
            local_k2 = float(arg)
    if (local_tweet_file == '' or local_queries_file == '' or local_frecuencies_file == '' or local_entity == ''):
        print(help_text)
        sys.exit(2)
    return local_tweet_file, local_queries_file, local_frecuencies_file, local_destination_dir, local_entity, local_b, local_k1, local_k2

def calculate_bm25(rt_bm25, r_bm25, nt_bm25, n_bm25, f_bm25, qf_bm25, k_bm25, k1_bm25, k2_bm25):
    '''Calculate BM25 of a term and document'''
    first_term = math.log10(((r_bm25 + 0.5)/(rt_bm25 - r_bm25 + 0.5)) / ((n_bm25 - r_bm25 + 0.5) / (nt_bm25 - n_bm25 + r_bm25 + 0.5)))
    second_term = ((k1_bm25 + 1) * f_bm25) / (k_bm25 + f_bm25)
    third_term = ((k2_bm25 + 1) * qf_bm25) / (k2_bm25 + qf_bm25)

    return first_term * second_term * third_term

def calculate_k(avdl, dl_document, b_bm25, k1_bm25):
    '''Calculate valeu of K'''
    return k1_bm25 * ((1 - b_bm25) + b_bm25 * (dl_document / avdl))

def main(tweet_file, queries_file, frecuencies_file, destination_dir, entity, b_var, k1_var, k2_var):
    '''Main function'''
    # Process tweet file
    tweets = []
    try:
        tweets = Tweets()
        tweets.load_file(tweet_file)
    except EnvironmentError as exception:
        print(exception)
        sys.exit(2)

    # Process queriesFile
    queries = []
    try:
        with open(queries_file) as query:
            csv_reader = csv.reader(query, delimiter='\t')
            for row in csv_reader:
                queries.append(Query(row))
    except EnvironmentError as exception:
        print(exception)
        sys.exit(2)

    # Process frecencies file.
    frecuencies = []
    try:
        frecuencies = Frecuencies()
        frecuencies.load_file(frecuencies_file)
    except EnvironmentError as exception:
        print(exception)
        sys.exit(2)

    # Calculamos los valores de bm25 y los goldstandard
    rt_var = 0 # Situamos estas a 0 por que no hay relevancia previa
    r_var = 0
    nt_var = 50000
    for query in queries:
        for tweet in tweets.documents:
            bm25 = 0
            np_terms = numpy.array(query.terms)
            for term in query.terms:
                n_var = frecuencies.get_term_frecuency(term)
                f_var = frecuencies.get_term_tweet_frecuency(term, tweet['id'])
                qf_var = numpy.count_nonzero(np_terms == term)
                k_var = calculate_k(tweets.get_average_length(), tweet['lenght'], b_var, k1_var)
                bm25 += calculate_bm25(rt_var, r_var, nt_var, n_var, f_var, qf_var, k_var, k1_var, k2_var)
            query.add_document(tweet['id'], bm25)
            query.set_goldstandard(tweets.get_goldstandard(query.identificator))

    # Borramos los ficheros
    gold_standard_result_path = destination_dir +'/gs_E'+entity+'.csv'
    if os.path.isfile(gold_standard_result_path):
        os.remove(gold_standard_result_path)
    ranking_result_path = destination_dir +'/rk_E'+entity+'.csv'
    if os.path.isfile(ranking_result_path):
        os.remove(ranking_result_path)

    # Escribimos el resultado en los ficheros.
    with open(gold_standard_result_path, 'a') as csv_goldstandard:
        csvwritter = csv.writer(csv_goldstandard, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)
        for query in queries:
            for row in query.get_goldstandard():
                csvwritter.writerow([query.identificator, row['tweet'], row['relevance']])

    with open(ranking_result_path, 'a') as csv_ranking:
        csvwritter = csv.writer(csv_ranking, delimiter="\t", quotechar='"', quoting=csv.QUOTE_ALL)
        for query in queries:
            for row in query.get_sorted_documents():
                csvwritter.writerow([query.identificator, row['document']])

if __name__ == "__main__":
    # Process arguments
    tweet_file_par, queries_file_par, frecuencies_file_par, destination_dir_par, entity_par, b_var_par, k1_var_par, k2_var_par = process_arguments(sys.argv[1:])
    main(tweet_file_par, queries_file_par, frecuencies_file_par, destination_dir_par, entity_par, b_var_par, k1_var_par, k2_var_par)

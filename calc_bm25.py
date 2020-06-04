#!/usr/bin/python
# pylint: disable=line-too-long

'''Main module of SINE practice about BM25 ranking of tweets'''

import sys
import getopt


def process_arguments(argv):
    '''Process script arguments and check if there an error'''

    tweet_file = ''
    queries_file = ''
    frecuencies_file = ''
    destination_file = ''
    local_k = ''
    local_k1 = ''
    local_k2 = ''
    try:
        opts, _ = getopt.getopt(argv, "ht:q:f:d:",
                                ["--tweetFile", "--queriesFile", "--frecuenciesFile", "--destinationFile", "--k1", "--k2", "--K"])
    except getopt.GetoptError:
        print('Help here')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Help here')
            sys.exit()
        elif opt in ("-t", "--tweetFile"):
            tweet_file = arg
        elif opt in ("-q", "--queriesFile"):
            queries_file = arg
        elif opt in ("-f", "--frecuenciesFile"):
            frecuencies_file = arg
    # TODO Tratar el retorno para que si no están los obligatorios pete.
    return tweet_file, queries_file, frecuencies_file, destination_file, local_k, local_k1, local_k2


tweetFile, queriesFile, frecuenciesFile, destinationFile, k, k1, k2 = process_arguments(sys.argv[1:])

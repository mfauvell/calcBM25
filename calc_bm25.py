#!/usr/bin/python
# pylint: disable=line-too-long

'''Main module of SINE practice about BM25 ranking of tweets'''

import sys
import getopt
import csv


def process_arguments(argv):
    '''Process script arguments and check if there an error'''

    help_text = 'Help here'
    tweet_file = ''
    queries_file = ''
    frecuencies_file = ''
    local_entity = ''
    destination_dir = 'result'
    local_k = ''
    local_k1 = ''
    local_k2 = ''
    try:
        opts, _ = getopt.getopt(argv, "ht:q:f:d:e:",
                                ["tweetFile=", "queriesFile=", "frecuenciesFile=", "destinationDir=", "entity=", "k1=", "k2=", "K="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    print(opts)
    for opt, arg in opts:
        print(opt)
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt in ("-t", "--tweetFile"):
            tweet_file = arg
        elif opt in ("-q", "--queriesFile"):
            queries_file = arg
        elif opt in ("-f", "--frecuenciesFile"):
            frecuencies_file = arg
        elif opt in ("-d", "--destinationDir"):
            destination_dir = arg
        elif opt in ("-e", "--entity"):
            local_entity = arg
        elif opt == "--K":
            local_k = arg
        elif opt == "--k1":
            local_k1 = arg
        elif opt == "--k2":
            local_k2 = arg
    if (tweet_file == '' or queries_file == '' or frecuencies_file == ''):
        print(help_text)
        sys.exit(2)
    return tweet_file, queries_file, frecuencies_file, destination_dir, local_entity, local_k, local_k1, local_k2


tweetFile, queriesFile, frecuenciesFile, destinationDir, entity, k, k1, k2 = process_arguments(sys.argv[1:])

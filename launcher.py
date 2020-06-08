#!/usr/bin/python

'''Launcher to all entities'''

import sys
import getopt
from multiprocessing import Process
import calc_bm25


def process_arguments(argv):
    '''Process script arguments and check if there an error'''

    help_text = 'Help here'
    local_b = ''
    local_k1 = ''
    local_k2 = ''
    try:
        opts, _ = getopt.getopt(argv, "h", ["k1=", "k2=", "b="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt == "--b":
            local_b = float(arg)
        elif opt == "--k1":
            local_k1 = float(arg)
        elif opt == "--k2":
            local_k2 = float(arg)
    return local_b, local_k1, local_k2

def execute(entity, b_var, k1_var, k2_var):
    '''Execute calc script'''
    tweet_file = "data/Tweets/RL2013D01E"+entity+".dat"
    queries_file = "data/Consultas/RL2013D01E"+entity+".dat"
    frecuencies_file = "data/Frecuencias/RL2013D01E"+entity+".dat"
    calc_bm25.main(tweet_file, queries_file, frecuencies_file,
                   'result', entity, b_var, k1_var, k2_var)

def main(b_var, k1_var, k2_var):
    '''Main function'''
    entities = ["001", "002", "003", "005", "008", "009", "012", "013", "014", "015",
                "016", "019", "022", "025", "033", "035", "040", "041", "043", "044"]
    process = {}
    for entity in entities:
        process[entity] = Process(target=execute, args=(entity, b_var, k1_var, k2_var))
        process[entity].start()

if __name__ == "__main__":
    # Process arguments
    b_var_par, k1_var_par, k2_var_par = process_arguments(sys.argv[1:])
    main(b_var_par, k1_var_par, k2_var_par)

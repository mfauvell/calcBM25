#!/usr/bin/python

'''Launcher to all entities'''

import sys
import getopt
import calc_bm25


def process_arguments(argv):
    '''Process script arguments and check if there an error'''

    help_text = 'Help here'
    local_k = ''
    local_k1 = ''
    local_k2 = ''
    try:
        opts, _ = getopt.getopt(argv, "h", ["k1=", "k2=", "K="])
    except getopt.GetoptError:
        print(help_text)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(help_text)
            sys.exit()
        elif opt == "--K":
            local_k = float(arg)
        elif opt == "--k1":
            local_k1 = float(arg)
        elif opt == "--k2":
            local_k2 = float(arg)
    return local_k, local_k1, local_k2

def main(k_var, k1_var, k2_var):
    '''Main function'''
    entities = ["001", "002", "003", "005", "008", "009", "012", "013", "014", "015",
                "016", "019", "022", "025", "033", "035", "040", "041", "043", "044"]
    for entity in entities:
        tweet_file = "data/Tweets/RL2013D01E"+entity+".dat"
        queries_file = "data/Consultas/RL2013D01E"+entity+".dat"
        frecuencies_file = "data/Frecuencias/RL2013D01E"+entity+".dat"
        calc_bm25.main(tweet_file, queries_file, frecuencies_file,
                       'result', entity, k_var, k1_var, k2_var)

if __name__ == "__main__":
    # Process arguments
    k_var_par, k1_var_par, k2_var_par = process_arguments(sys.argv[1:])
    main(k_var_par, k1_var_par, k2_var_par)

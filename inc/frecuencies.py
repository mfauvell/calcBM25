'''File with frecuencies class'''

import csv

class Frecuencies:
    '''Class that represents the frecuencies of terms in total and per tweet'''

    def __init__(self):
        self.frecuencies = {}

    def load_file(self, file):
        '''Load a file with frecuencies'''
        with open(file) as frec_file:
            csv_reader = csv.reader(frec_file, delimiter='\t')
            for row in csv_reader:
                print('row')
                print(row)
                term = row[0]
                total_frec = row[1]
                tweets = {}
                if row[2] != '':
                    tweets_base = row[2].strip(";").split(";")
                    print(tweets_base)
                    for tweet in tweets_base:
                        components = tweet.strip(",").split(",")
                        tweets[components[0]] = components[1]
                self.frecuencies[term] = {'frec': total_frec, 'tweets': tweets}

    def get_term_frecuency(self, term):
        '''Get the total frecuency of a term'''
        if term in self.frecuencies:
            return self.frecuencies[term]['frec']
        return 0

    def get_term_tweet_frecuency(self, term, tweet_id):
        '''Get the frecuency of a term in a tweet'''
        if term in self.frecuencies:
            if tweet_id in self.frecuencies[term]['tweets']:
                return self.frecuencies[term]['tweets'][tweet_id]
        return 0

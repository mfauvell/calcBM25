'''File with tweets class'''

import csv

class Tweets:
    '''Class that represents a list of tweets with the query related'''

    def __init__(self):
        self.documents = []


    def load_file(self, file):
        '''Load a file with tweets'''
        with open(file) as tweet_file:
            csv_reader = csv.reader(tweet_file, delimiter='\t')
            for row in csv_reader:
                self.documents.append({'id': row[0], 'query': row[2]})

    def get_goldstandard(self, query_id):
        '''Return and array of goldstandard for query id'''
        goldstandard = []
        for tweet in self.documents:
            if tweet.query == query_id:
                goldstandard.append({'tweet': tweet.id, 'relevance': 1})
            else:
                goldstandard.append({'tweet': tweet.id, 'relevance': 0})
        return goldstandard

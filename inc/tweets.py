'''File with tweets class'''

import csv

class Tweets:
    '''Class that represents a list of tweets with the query related'''

    def __init__(self):
        self.documents = []
        self.average_length = 0

    def load_file(self, file):
        '''Load a file with tweets'''
        with open(file) as tweet_file:
            csv_reader = csv.reader(tweet_file, delimiter='\t')
            for row in csv_reader:
                self.documents.append({'id': row[0], 'query': row[2],
                                       'lenght': len(row[1].split())})

    def get_goldstandard(self, query_id):
        '''Return and array of goldstandard for query id'''
        goldstandard = []
        for tweet in self.documents:
            if int(tweet['query']) == int(query_id):
                goldstandard.append({'tweet': tweet['id'], 'relevance': 1})
            else:
                goldstandard.append({'tweet': tweet['id'], 'relevance': 0})
        return goldstandard

    def get_average_length(self):
        '''Return average lenght of tweets'''
        if self.average_length == 0:
            self.average_length = float(
                sum(d['lenght'] for d in self.documents)) / len(self.documents)
        return self.average_length

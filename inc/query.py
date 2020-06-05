'''File with Query Class'''

import operator

class Query:
    '''Query class to collect all data of queries'''

    def __init__(self, row):
        self.identificator = row[0]
        self.terms = row[1].strip(";").split(";")
        self.gold_standard = ''
        self.documents = []

    def get_goldstandard(self):
        '''Retreives goldstandard array'''
        return self.gold_standard

    def set_goldstandard(self, gold_standard):
        '''Set a array like goldstandard of query'''
        self.gold_standard = gold_standard

    def add_document(self, document, value):
        '''Adds a document to array of documents'''
        self.documents.append({'document': document, 'value': value})

    def get_sorted_documents(self):
        '''Return a list of documents sorted by value'''
        return sorted(self.documents, key=operator.itemgetter('value'), reverse=True)

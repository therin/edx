import string
import time
from ps6 import *


class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def isWordIn(self, text):
        word_0 = self.word
        self.text = text
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        raise NotImplementedError
        """
        word_1 = word_0.lower()
        text_1 = text.lower()
        for l in text_1:
            if l is string.punctuation:
                text_1.replace(l," ")
        text_2 = text_1.split(" ")
        for w in text_2:
            if w == word_1:
                return True
            else:
                return False

s2  = TitleTrigger('soft')
s2.evaluate(koala)
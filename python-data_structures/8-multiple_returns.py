#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = len(sentence)
    if len(sentence) < 0:
        return None
    return len(sentence) + range("0")
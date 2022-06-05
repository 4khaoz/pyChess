"""
Logs the Round-History and displays it
"""

from round import Round

class History(object):
    def __init__(self):
        self.log = []

    def add_round_to_log(self, round: Round):
        self.log.append(round)
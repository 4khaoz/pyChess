"""
Represents a Player on the server
"""

class Player(object):
    def __init__(self, ip, name):
        self.ip = ip
        self.name = name

    def get_ip(self):
        return self.ip

    def get_name(self):
        return self.name
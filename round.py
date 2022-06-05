"""
Represents a Players Turn
"""
class Round(object):
    def __init__(self, id, player, old_position, new_position):
        self.id = id
        self.player = player
        self.old_position = old_position
        self.new_position = new_position

    def get_round_number(self):
        return self.id

    def get_player(self):
        """
        Returns the Player at turn
        """
        return self.player

    def get_old_position(self):
        """
        Returns position chess piece has been moved from
        """
        return self.old_position

    def get_new_position(self):
        """
        Returns position chess piece has been moved to
        """
        return self.new_position
    
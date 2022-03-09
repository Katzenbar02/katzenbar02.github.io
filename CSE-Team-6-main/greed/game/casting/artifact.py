from game.casting.actor import Actor


class Artifact(Actor):
    """
    An item of cultural or historical interest. 
    
    The responsibility of an Artifact is to provide a message about itself.

    Attributes:
        _message (string): A short description about the artifact.
    """
    def __init__(self):
        super().__init__()
        self._value = 0
        
    def get_value(self):
        """Gets the artifact's value.
        
        Returns:
            string: The value.
        """
        return self._value
    
    def set_value(self, text):
        """Updates the value to the given one
            dependent on the text being a * or O.

            * = gem
            O = Rock
        Args:
            value (string): The given value.
        """
        if text == '*':
            value = 1
        elif text == 'O':
            value = -1
        self._value = value
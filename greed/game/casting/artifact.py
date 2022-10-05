from game.casting.actor import Actor

class Artifact(Actor):
    """ A visible static item that exists on the playing board and keeps track of it's points depending on if it's a rock or gem
    (inherits from actor())

    The responsiblity of an artifact is to be randomly positioned on the screen and start down the screen and remember its position
      and what it is, or rather what it will tell the Robot it is when interogated by the Director

    Attributes:
        _message
        Inherits and uses from Actor:
            _text (string): The text to display
            _font_size (int): The font size to use.
            _color (Color): The color of the text.
            _position (Point): The screen coordinates.
            _velocity (Point): The speed and direction.
    
    """

    def __init__(self):
        """
        Constructs a new Artifact, inheriting from Actor 
        """
        super().__init__()
        self._points = 0
    
    def get_points(self):
        if self.get_text() == '*':
            self.points = 1
        else:
            self.points = -1
        return self.points
class Atom:
    """ an atom with a number, symbol, and coordinates. """

    def __init__(self, num: int, sym: str, x: float, y: float, z: float) -> None:
        """ Create an Atom with number num, string symbol sym, and float
        coordinates (x, y, z)
        """

        self.number = num
        self.center = (x, y, z)
        self.symbol = sym


    def __str__(self) -> str:
        """ return a string rep of this atom in this format
        (SYMBOL, x, y, z)
        """
        return "({0}, {1}, {2}, {3})".format(
            self.symbol, self.center[0], self.center[1], self.center[2])

    def __repr__(self) -> str:
        """ Return a string rep of this atom in this Atom in this format:
            Atom(NUMBER, "SYMBOL", X, Y, Z)
        """

        return 'Atom({0}, "{1}", {2}, {3}, {4})'.format(
            self.number, self.symbol,
            self.center[0], self.center[1], self.center[2])


    def translate(self, x: float, y: float, z: float) -> None:
        """ Move this Atom by adding (x, y, z) to its coordinates.
        """

        self.center = (self.center[0] + x,
                       self.center[1] + y,
                       self.center[2] + z)
        

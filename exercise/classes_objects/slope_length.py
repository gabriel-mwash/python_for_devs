class Point:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class LineSegment:
    def __init__(self, point1, point2) -> None:
        self.startpoint = point1
        self.endpoint = point2

        
    def slope(self) -> float:
        return (self.endpoint.y - self.startpoint.y) / \
               (self.endpoint.x - self.startpoint.x)


    def length(self) -> float:
        return math.sqrt(
        (self.endpoint.x - self.startpoint.x) ** 2 +
        (self.endpoint.y - self.startpoint.x) ** 2)

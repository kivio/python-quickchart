"""
    Here you can find simple class that is required to set up the chart.
"""

from PIL import ImageColor

class Resolution(object):
    """
        Resolution class represent settings of chart resolution in pixels

        Resolution object may cast to tuple, example:
        >> r = Resolution(800, 600)
        >> tuple(r)
        (800,600)

        Attrs:
            width : width of chart
            height : height of chart
    """

    __slots__ = ['width', 'height']

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __cmp__(self, other):
        if self.width == other.width and self.height == other.height:
            return True
        return False

    def __eq__(self, other):
        return self.__cmp__(other)

    def __iter__(self):
        yield self.width
        yield self.height

    def get_center(self):
        """
            return center of image with that resolution
        """
        return Point(self.width // 2, self.height // 2)

class Point(object):
    """
        Point class represent point coordinates

        Attrs:
            x : x coordinate of point
            y: y coordinate of point
    """

    __slots__ = ['x','y']

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y

class Color(object):
    """
        Color class represent RGB color with simple initialize.
        You may create color from tuple of web standard

        Color class may cast to tuple, example:
        >> c = Color('#fff')
        >> tuple(c)
        (255,255,255)

        Attrs:
            r : Red color (0 - 255)
            g : Green color (0 - 255)
            b : Blue color (0 - 255)
    """

    __slots__ = ['r','g','b']

    def __init__(self, color):
        if isinstance(color, tuple):
            self.r, self.g, self.b = color
        elif isinstance(color, basestring):
            self.r, self.g, self.b = ImageColor.getrgb(color)
        else:
            raise ValueError

    def __iter__(self):
        yield self.r
        yield self.g
        yield self.b
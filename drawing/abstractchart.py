"""
    .. moduleauthor:: Marcin Karkocha <kivio@kivio.pl>

    AbstractPlot is class to draw coordinate system (Cartesian is default)

    configuration options:
    - arrows: color, direction, shape
    - line size and color
    - scale - named and unnamed, size, color
    - axis names - font, size, location
"""

from tools import Resolution, Color, Point
from PIL import Image, ImageDraw

class AbstractPlot(object):

    def __init__(self):
        """
            AbstractPlot is a class to draw coordinate system
        """
        self._coordinates_thickness = 2
        self._grid_padding = 20
        self._grid_color = Color('#A5C9FF')
        self._resolution = Resolution(800,600)
        self._image = Image.new('RGB', tuple(self._resolution), tuple(Color('#fff')))

    def get_resolution(self):
        """
            return resolution of plot (Resolution object)
        """
        return self._resolution

    def _get_center(self):
        """
            This is interface who calculate center of plot, by default is center of available space
        """
        return self._resolution.get_center()

    def _draw_coordinates(self, draw):
        """
            this method draw coordinates line
        """
        center = self._get_center()
        draw.line([(center.x,0),(center.x, self._resolution.height)],
            fill = tuple(Color('#394659')), width = self._coordinates_thickness)
        draw.line([(0,center.y),(self._resolution.width, center.y)],
            fill = tuple(Color('#394659')), width = self._coordinates_thickness)

    def _draw_grid(self, draw):
        """
            this method draw grid
        """
        width, height = tuple(self._resolution)
        vertical_lines = (((x, 0),(x, height)) \
            for x in xrange(self._grid_padding, width, self._grid_padding))
        horizontal_lines = (((0, y), (width, y)) \
            for y in xrange(self._grid_padding, height, self._grid_padding))

        draw_line = lambda points: draw.line(points, fill = tuple(self._grid_color), width = 1)
        map(draw_line, vertical_lines)
        map(draw_line, horizontal_lines)

    def _draw(self):
        """
            this method draw all elements of chart
        """
        draw = ImageDraw.ImageDraw(self._image)
        self._draw_grid(draw)
        self._draw_coordinates(draw)
        del draw

    def save_as_png(self, file_path):
        """
            save created image to file (now is draw all part of chart with actual settings)
        """
        self._draw()
        self._image.save(file_path, "PNG")

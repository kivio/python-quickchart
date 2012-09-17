"""
    .. moduleauthor:: Marcin Karkocha <kivio@kivio.pl>

    AbstractChart is class to draw coordinate system (Cartesian is default)

    configuration options:
    - arrows: color, direction, shape
    - line size and color
    - scale - named and unnamed, size, color
    - axis names - font, size, location
"""

class AbstractChart(object):

    def __init__(self, data):
        """
            Args:
                data list: for charts that inheritance this class is data set to draw
        """
        self._data = data

    def _get_center(self):
        """
            This is abstract method who calculate coordinates to chart

            Raises:
                NotImplementedError
        """
        raise NotImplementedError
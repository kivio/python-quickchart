"""
    unittest to AbstractChart class
"""

import unittest
from unittest import TestCase

import os

from tools import Point, Resolution
from drawing.abstractchart import AbstractPlot

class TestAbstractChart(TestCase):

    def setUp(self):
        self.abstract_plot = AbstractPlot()
        self.path = '/tmp/abstract.png'

    def test_resolution(self):
        self.assertEqual(self.abstract_plot.get_resolution(), Resolution(800,600))

    def test_save(self):
        self.abstract_plot.save_as_png(self.path)
        self.assertTrue(os.path.isfile(self.path))
        os.remove(self.path)

if __name__ == '__main__':
    unittest.main()
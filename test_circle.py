"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


class CircleTest(unittest.TestCase):
    """Tests of the Circle class."""

    def setUp(self):
        """Create a circle before each test."""
        self.circle = Circle(1)
        self.circle2 = Circle(10)

    def test_add_area_typical_values(self):
        """
        Typical case:
        Test add_area with two circles having positive radii.
        """
        result = self.circle.add_area(self.circle2)
        self.assertEqual(result.get_radius(), 10.04987562112089)

    def test_add_area_for_radius_zero(self):  # edge case
        """
        Edge case:
        Test add_area when one of the circles has radius 0,
        the other has non-zero radius.
        (Result should have same radius.)
        Does add_area work the same regardless of
        which circle has radius 0?
        """
        self.circle_zero = Circle(0)
        result = self.circle.add_area(self.circle_zero)
        self.assertEqual(result.get_radius(), 1)

    def test_negative_radius(self):
        """Circle constructor raises exception if the radius is negative."""
        self.neg_circle = Circle(-1)
        with self.assertRaises(ValueError):
            self.neg_circle.get_radius()

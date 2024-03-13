"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class CounterTest(unittest.TestCase):
    """Tests of the Counter class."""
    def setUp(self):
        """Create a circle before each test."""
        self.c1 = Counter()
        self.c2 = Counter()

    def test_counter_increment(self):
        """Test that counter is count correctly."""
        self.c1.increment()
        self.assertEqual(self.c1.count, 2)
        self.assertEqual(self.c2.count, 2)

    def test_is_singleton(self):
        """Test that Counter is a singleton."""
        self.assertIs(self.c1, self.c2)

    def test_count_not_reset(self):
        """Test that count is not reset to 0 when you invoke count = Counter() after the first time."""
        initial_count = self.c1.count
        new_counter = Counter()
        self.assertIs(new_counter.count, initial_count)

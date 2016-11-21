from unittest import TestCase
from p0001 import empty


class TestSolution(TestCase):
    def test_empty(self):
        self.assertEquals(empty(), "")

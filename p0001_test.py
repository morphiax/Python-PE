from unittest import main
from unittest import TestCase
from p0001 import empty


class TestSolution(TestCase):
    def test_empty(self):
        self.assertEqual(empty(), "")
        
if __name__ == "__main__":
	main()

import time
import unittest
from unittest.mock import patch
from io import StringIO
from decorator import mean


class TestMeanDecorator(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_mean_decorator(self, mock_stdout):
        @mean(3)
        def some_function():
            time.sleep(0.1)

        for _ in range(3):
            some_function()
        output_lines = mock_stdout.getvalue().split('\n')
        print(output_lines)
        last_line = output_lines[-2]
        average_time = float(last_line.split()[-2])
        self.assertAlmostEqual(average_time, 0.1, delta=0.03)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mean_decorator_with_no_calls(self, mock_stdout):
        @mean(3)
        def some_function():
            pass

        some_function()

        output_lines = mock_stdout.getvalue().split('\n')
        last_line = output_lines[-2]
        average_time = float(last_line.split()[-2])

        self.assertAlmostEqual(average_time, 0.0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mean_decorator_with_large_k(self, mock_stdout):
        @mean(5)
        def some_function():
            time.sleep(0.3)

        for _ in range(4):
            some_function()
        output_lines = mock_stdout.getvalue().split('\n')
        last_line = output_lines[-2]
        average_time = float(last_line.split()[-2])
        self.assertAlmostEqual(average_time, 0.3, delta=0.05)

import unittest
from unittest.mock import patch

from message_estimating import SomeModel, predict_message_mood


class TestEstimating(unittest.TestCase):

    def test_excellent_mark(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.9
            self.assertEqual(predict_message_mood("some string", model), "отл")

    def test_bad_mark(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.1
            self.assertEqual(
                predict_message_mood("some string", model),
                "неуд"
            )

    def test_ok_mark(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.4
            self.assertEqual(
                predict_message_mood("some string", model),
                "норм"
            )

    def test_corner_between_bad_and_ok(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.3
            self.assertEqual(
                predict_message_mood("some string", model),
                "норм"
            )

    def test_corner_between_excellent_and_ok(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.8
            self.assertEqual(
                predict_message_mood("some string", model),
                "норм"
            )

    def test_input_error(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = "Я вернул строку и что ты мне сделаешь"
            with self.assertRaises(TypeError):
                predict_message_mood("some string", model)

    def test_too_big_predict(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 2
            with self.assertRaises(ValueError):
                predict_message_mood("some string", model)

    def test_too_small_predict(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = -1
            with self.assertRaises(ValueError):
                predict_message_mood("some string", model)

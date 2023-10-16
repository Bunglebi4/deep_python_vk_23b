import unittest
from unittest.mock import patch, MagicMock

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
                predict_message_mood("some string", model, good_thresholds=0.8,
                                     bad_thresholds=0.3),
                "норм"
            )

    def test_right_corner(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 1
            self.assertEqual(
                predict_message_mood("some string", model),
                "отл"
            )

    def test_left_corner(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0
            self.assertEqual(
                predict_message_mood("some string", model),
                "неуд"
            )

    def test_corner_between_excellent_and_ok(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.8
            self.assertEqual(
                predict_message_mood("some string", model, good_thresholds=0.8,
                                     bad_thresholds=0.3),
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

    def test_thresholds_changing(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.8
            self.assertEqual(
                predict_message_mood(
                    "some string", model, 0.1, 0.5),
                "отл"
            )

    def test_bad_thresholds(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.8
            with self.assertRaises(ValueError):
                predict_message_mood(
                    "some string", model, -2, 23.0)

    def test_predict_arguments(self):
        model = SomeModel()
        model.predict = MagicMock()
        message = "message"
        model.predict(message)
        model.predict.assert_called_with(message)

    @patch('message_estimating.SomeModel.predict', mock=MagicMock())
    def test_predict_arguments_in_message_mood(self, mock):
        model = SomeModel()
        mock.return_value = 0.5
        message = "message"
        self.assertEqual(predict_message_mood(message, model), "норм")
        mock.assert_called_with(message)

    def test_near_right_corner(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0 + 0.01 ** 100
            self.assertEqual(
                predict_message_mood("some string", model),
                "неуд"
            )

    def test_near_left_corner(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.1 ** 10
            self.assertEqual(
                predict_message_mood("some string", model),
                "неуд"
            )

    def test_near_corner_threshold_between_good_and_exc(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.8 - 0.1 ** 10
            self.assertEqual(predict_message_mood("some string", model),
                             "норм")
            mock.return_value = 0.8 + 0.1 ** 10
            self.assertEqual(predict_message_mood("some string", model),
                             "отл")

    def test_near_corner_threshold_between_good_and_bad(self):
        model = SomeModel()
        with patch("message_estimating.SomeModel.predict") as mock:
            mock.return_value = 0.3 - 0.1 ** 10
            self.assertEqual(predict_message_mood("some string", model),
                             "неуд")
            mock.return_value = 0.3 + 0.1 ** 10
            self.assertEqual(predict_message_mood("some string", model),
                             "норм")

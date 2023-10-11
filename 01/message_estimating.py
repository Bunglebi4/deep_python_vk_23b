import random


class SomeModel:

    def predict(self, message: str) -> float:
        return random.random()


def predict_message_mood(
        message: str,
        model: SomeModel,
        bad_thresholds: float = 0.3,
        good_thresholds: float = 0.8,
) -> str:
    if bad_thresholds < 0 or good_thresholds > 1:
        raise ValueError("Unexpected thresholds")
    prediction = model.predict(message)
    if prediction < 0 or prediction > 1:
        raise ValueError("Unexpected prediction")
    if prediction < bad_thresholds:
        return "неуд"
    if prediction > good_thresholds:
        return "отл"
    return "норм"

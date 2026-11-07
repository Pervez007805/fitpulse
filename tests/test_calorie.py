import pytest

from fitpulse.calorie import bmr, get_strategy


def test_bmr_formula():
    assert bmr(80, 175, 21) == 1793.75


def test_weight_loss_target_for_sample_user():
    assert round(get_strategy("weight loss").calculate(80, 175, 21)) == 2011


def test_muscle_gain_is_300_above_maintenance():
    maintenance = get_strategy("maintenance").calculate(80, 175, 21)
    gain = get_strategy("muscle gain").calculate(80, 175, 21)
    assert gain - maintenance == pytest.approx(300)


def test_weight_loss_is_500_below_maintenance():
    maintenance = get_strategy("maintenance").calculate(80, 175, 21)
    loss = get_strategy("weight loss").calculate(80, 175, 21)
    assert maintenance - loss == pytest.approx(500)


def test_unknown_goal_raises():
    with pytest.raises(ValueError):
        get_strategy("bulk up")

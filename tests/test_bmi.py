from fitpulse.bmi import bmi_category, calculate_bmi


def test_sample_user_bmi_is_26_1():
    assert calculate_bmi(80, 175) == 26.1


def test_sample_user_category_is_overweight():
    assert bmi_category(calculate_bmi(80, 175)) == "Overweight"


def test_categories():
    assert bmi_category(17.0) == "Underweight"
    assert bmi_category(18.5) == "Normal"
    assert bmi_category(24.9) == "Normal"
    assert bmi_category(27.0) == "Overweight"
    assert bmi_category(31.0) == "Obese"

import pytest

from fitpulse.diet import build_diet_plan, plan_total
from fitpulse.workouts import WorkoutFactory, build_workout_plan


def test_factory_creates_each_type():
    assert WorkoutFactory.create("cardio").kind == "Cardio"
    assert WorkoutFactory.create("Strength").kind == "Strength"
    assert WorkoutFactory.create("YOGA").kind == "Yoga"


def test_factory_rejects_unknown_type():
    with pytest.raises(ValueError):
        WorkoutFactory.create("swimming")


def test_workout_plan_depends_on_goal():
    kinds = [w.kind for w in build_workout_plan("weight loss")]
    assert kinds == ["Cardio", "Strength"]


def test_diet_plan_matches_target():
    meals = build_diet_plan(2011)
    assert len(meals) == 4
    assert abs(plan_total(meals) - 2011) <= 2

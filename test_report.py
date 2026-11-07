from datetime import date

from fitpulse.report import build_report, day_summary


def test_day_summary_matches_lab_example():
    s = day_summary(770, 300, 2011)
    assert s["net"] == 470
    assert s["remaining"] == 1541


def test_day_summary_without_target():
    assert day_summary(500, 100, None)["remaining"] is None


def test_weekly_report_only_counts_last_seven_days():
    totals = {
        date(2026, 11, 1): (1000.0, 200.0),
        date(2026, 11, 2): (2500.0, 100.0),
        date(2026, 10, 1): (9999.0, 0.0),  # outside the week, must be ignored
    }
    r = build_report(totals, 2011, 7, date(2026, 11, 2), "Weekly")
    assert r["days_logged"] == 2
    assert r["total_consumed"] == 3500
    assert r["avg_consumed"] == 1750
    assert r["goal_days"] == 1  # only 1000 kcal is within the 2011 target

# FitPulse: Fitness and Diet Tracking System

Semester project for Software Construction and Development (SCD), MUET SZAB Campus Khairpur.
Student: Pervez Parhyar (K24SW007). Teacher: Umrah Zadi.

Language: **Python 3.10+**. Database: **MySQL 8.0**. GUI: **Tkinter**. Tests: **PyTest**.

## Features
1. Signup / Login (passwords stored as salted PBKDF2 hashes)
2. User profile (age, weight, height, goal)
3. BMI calculator with category
4. Daily calorie target (Strategy pattern: weight loss, muscle gain, maintenance)
5. Workout plan (Factory pattern: Cardio, Strength, Yoga)
6. Diet plan with meal calories matched to the target
7. Daily tracker (add / delete meals and exercises, net and remaining calories)
8. Weekly and monthly progress report with a bar chart

## Documentation
| Document | Location |
|---|---|
| Project proposal | `docs/FitPulse_Project_Proposal.pdf` |
| Software Requirements Specification (SRS) | `docs/FitPulse_SRS.pdf` |
| UML diagrams (use case, activity, class, object) | `docs/uml/` |
| Clickable HTML prototype (open the file in a browser; demo login `pervez@example.com` / `demo1234`) | `docs/prototype/fitpulse_prototype.html` |

<!-- Add screenshots of the running app to docs/screenshots/ and uncomment these lines:
## Screenshots
![Login](docs/screenshots/login.png)
![Profile](docs/screenshots/profile.png)
![Tracker](docs/screenshots/tracker.png)
![Report](docs/screenshots/report.png)
-->

## Design patterns and where they are
| Pattern | File |
|---|---|
| Strategy | `src/fitpulse/calorie.py` |
| Factory | `src/fitpulse/workouts.py` |
| Singleton | `src/fitpulse/db/connection.py` |
| Repository | `src/fitpulse/repositories.py` |

Layers: UI (`ui/app.py`) -> services (`services.py`, `auth.py`) -> repositories -> MySQL.

## Setup (one time)
1. Install Python 3.10+ and MySQL 8.0 (MySQL must be running).
2. Create the database. In the MySQL shell or MySQL Workbench run:
   `CREATE DATABASE fitpulse;`
3. Copy `config/config.example.ini` to `config/config.ini` and set your MySQL user and password.
   (`config.ini` is git-ignored, so your password is never uploaded to GitHub.)
   You can also set the password with the environment variable `FITPULSE_DB_PASSWORD`.
4. Install the libraries:
   `pip install -r requirements.txt`

## Run the application
    python run.py

The tables are created automatically on the first run (from `sql/schema.sql`).

## Run the tests
    pytest

The tests cover BMI, calorie strategies, workout and diet plans, the report, validation and
signup/login (using a fake in-memory store, so MySQL is not needed for tests).

Acceptance check (SRS 6.5): sample user 80 kg, 175 cm, age 21, weight loss gives
BMI 26.1 (Overweight) and a calorie target of 2011 kcal.

## Project structure
```
fitpulse/
├── run.py                      start the app
├── config/config.example.ini   copy to config.ini and add your MySQL password
├── sql/schema.sql              MySQL tables
├── requirements.txt
├── pytest.ini
├── docs/                       proposal, SRS, UML diagrams, prototype, screenshots
├── src/fitpulse/
│   ├── main.py                 startup (schema check, wiring)
│   ├── config.py               reads config.ini
│   ├── models.py               User and GOALS
│   ├── validation.py           input rules (SRS FR-2, FR-1)
│   ├── security.py             password hashing
│   ├── bmi.py                  BMI and category (FR-3)
│   ├── calorie.py              Strategy pattern (FR-4)
│   ├── workouts.py             Factory pattern (FR-5)
│   ├── diet.py                 diet plan (FR-6)
│   ├── report.py               daily summary and weekly/monthly report (FR-7, FR-8)
│   ├── auth.py                 signup and login (FR-1)
│   ├── repositories.py         database access (Repository pattern)
│   ├── services.py             business logic used by the UI
│   ├── db/connection.py        Singleton database connection and schema setup
│   └── ui/app.py               Tkinter screens
└── tests/                      PyTest unit tests
```

## Git (recommended)
    git init
    git add .
    git commit -m "feat: project skeleton"
Use small commits with clear messages, for example `feat: add calorie strategies`.

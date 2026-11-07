-- FitPulse schema for MySQL 8.0
-- The database itself is created first (see README).
CREATE TABLE IF NOT EXISTS users (
    id            INT AUTO_INCREMENT PRIMARY KEY,
    full_name     VARCHAR(100) NOT NULL,
    email         VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    age           INT NULL,
    weight        DOUBLE NULL,
    height        DOUBLE NULL,
    goal          VARCHAR(20) NULL,
    created_at    TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS daily_logs (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    user_id   INT NOT NULL,
    log_date  DATE NOT NULL,
    UNIQUE KEY uq_user_day (user_id, log_date),
    CONSTRAINT fk_log_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS meals (
    id        INT AUTO_INCREMENT PRIMARY KEY,
    log_id    INT NOT NULL,
    name      VARCHAR(60) NOT NULL,
    calories  DOUBLE NOT NULL,
    CONSTRAINT fk_meal_log FOREIGN KEY (log_id) REFERENCES daily_logs(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS exercises (
    id              INT AUTO_INCREMENT PRIMARY KEY,
    log_id          INT NOT NULL,
    name            VARCHAR(60) NOT NULL,
    calories_burned DOUBLE NOT NULL,
    CONSTRAINT fk_ex_log FOREIGN KEY (log_id) REFERENCES daily_logs(id) ON DELETE CASCADE
);

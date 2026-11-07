import pytest

from fitpulse.auth import AuthError, AuthService
from fitpulse.models import User
from fitpulse.validation import ValidationError, validate_profile


class FakeStore:
    """In-memory replacement for UserRepository, so tests need no MySQL."""

    def __init__(self):
        self.users = []

    def create(self, user):
        user.id = len(self.users) + 1
        self.users.append(user)
        return user.id

    def find_by_email(self, email):
        return next((u for u in self.users if u.email == email), None)


def test_signup_then_login():
    store = FakeStore()
    auth = AuthService(store)
    auth.signup("Pervez Parhyar", "Pervez@Example.com", "secret1", "secret1")
    user = auth.login("pervez@example.com", "secret1")
    assert user.full_name == "Pervez Parhyar"


def test_password_is_not_stored_in_plain_text():
    store = FakeStore()
    AuthService(store).signup("A B", "a@b.com", "secret1", "secret1")
    assert store.users[0].password_hash != "secret1"


def test_wrong_password_rejected():
    store = FakeStore()
    auth = AuthService(store)
    auth.signup("A B", "a@b.com", "secret1", "secret1")
    with pytest.raises(AuthError):
        auth.login("a@b.com", "wrong")


def test_duplicate_email_rejected():
    store = FakeStore()
    auth = AuthService(store)
    auth.signup("A B", "a@b.com", "secret1", "secret1")
    with pytest.raises(AuthError):
        auth.signup("C D", "a@b.com", "secret2", "secret2")


def test_password_mismatch_rejected():
    with pytest.raises(ValidationError):
        AuthService(FakeStore()).signup("A B", "a@b.com", "secret1", "secret2")


def test_profile_ranges_enforced():
    with pytest.raises(ValidationError):
        validate_profile(5, 80, 175, "weight loss")
    with pytest.raises(ValidationError):
        validate_profile(21, 80, 175, "bulk up")
    assert validate_profile("21", "80", "175", "Weight Loss") == (21, 80.0, 175.0, "weight loss")

import pytest

from main import hash_pin, is_account_number_valid, is_nominal_valid, verify_pin


@pytest.mark.parametrize(
    "nomor_rekening, expected",
    [
        ("1234567890", True),
        ("9876543210123456", True),
        ("12345", False),
        ("12345678901234567", False),
        ("12345ABCDE", False),
        ("", False),
    ],
)
def test_is_account_number_valid(nomor_rekening, expected):
    assert is_account_number_valid(nomor_rekening) == expected


@pytest.mark.parametrize(
    "nominal, expected",
    [
        (50000, True),
        (50_000_000, True),
        (0, False),
        (-1000, False),
        (50_000_001, False),
    ],
)
def test_is_nominal_valid(nominal, expected):
    assert is_nominal_valid(nominal) == expected


def test_hash_pin_tidak_sama_dengan_pin_asli():
    pin = "123456"
    assert hash_pin(pin) != pin


def test_verify_pin_benar():
    pin = "123456"
    hashed = hash_pin(pin)
    assert verify_pin(pin, hashed) is True


def test_verify_pin_salah():
    pin = "123456"
    hashed = hash_pin(pin)
    assert verify_pin("654321", hashed) is False

import pytest

from main import is_account_number_valid, is_nominal_valid


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

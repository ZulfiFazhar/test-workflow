import re

MAKSIMUM_NOMINAL_HARIAN = 50_000_000


def is_account_number_valid(nomor_rekening: str) -> bool:
    """Validasi nomor rekening bank.

    Nomor rekening dianggap valid jika terdiri dari 10-16 digit angka
    saja (tanpa spasi, huruf, atau simbol).
    """
    return bool(re.fullmatch(r"\d{10,16}", nomor_rekening))


def is_nominal_valid(nominal: float) -> bool:
    """Validasi nominal transaksi.

    Nominal dianggap valid jika bertipe numerik, lebih besar dari 0,
    dan tidak melebihi batas transaksi harian (Rp 50.000.000).
    """
    if isinstance(nominal, bool) or not isinstance(nominal, (int, float)):
        return False
    return 0 < nominal <= MAKSIMUM_NOMINAL_HARIAN


def main():
    print("Hello from test-workflow!")


if __name__ == "__main__":
    main()

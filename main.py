import re


def is_account_number_valid(nomor_rekening: str) -> bool:
    """Validasi nomor rekening bank.

    Nomor rekening dianggap valid jika terdiri dari 10-16 digit angka
    saja (tanpa spasi, huruf, atau simbol).
    """
    return bool(re.fullmatch(r"\d{10,16}", nomor_rekening))


def main():
    print("Hello from test-workflow!")


if __name__ == "__main__":
    main()

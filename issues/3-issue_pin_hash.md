# [Security] Implementasi Hashing PIN Transaksi

## Deskripsi

Menyimpan PIN transaksi dalam bentuk _plain text_ adalah celah
keamanan fatal (OWASP Top 10). PIN harus di-_hash_ sebelum disimpan
ke database.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Security] Implementasi Hashing PIN Transaksi" \
     --body-file issues/3-issue_pin_hash.md \
     --label "security"
   ```

   Catat nomor issue yang dihasilkan, lalu gunakan nomor tersebut pada
   branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format
   `feature/issue-<nomor>-pin-hash`.

## Tugas

1. Gunakan pustaka `bcrypt` yang sudah ditambahkan ke proyek.
2. Buat fungsi `hash_pin(pin: str) -> str` di `main.py`.
3. Buat fungsi `verify_pin(plain_pin: str, hashed_pin: str) -> bool`.

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `test_main.py` untuk memastikan:

- Hasil dari `hash_pin` tidak sama dengan PIN aslinya.
- `verify_pin` mengembalikan `True` jika disuntikkan PIN asli dan hash-nya.
- `verify_pin` mengembalikan `False` jika disuntikkan PIN yang salah.

## Instruksi CI/CD

Jalankan `uv run pytest` di lokal sebelum membuat PR. Pipeline GitHub
Actions harus hijau.

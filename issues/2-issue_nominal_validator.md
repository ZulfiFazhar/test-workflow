# [Feature] Penambahan Validasi Nominal Transaksi

## Deskripsi

Setiap transaksi harus memiliki nominal yang valid: berupa angka
positif dan tidak melebihi batas maksimum transaksi harian.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Feature] Penambahan Validasi Nominal Transaksi" \
     --body-file issues/2-issue_nominal_validator.md \
     --label "feature"
   ```

   Catat nomor issue yang dihasilkan, lalu gunakan nomor tersebut pada
   branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format
   `feature/issue-<nomor>-nominal-validator`.

## Tugas

1. Buat fungsi `is_nominal_valid(nominal: float) -> bool` di `main.py`.
2. Nominal dianggap valid jika:
   - Bertipe numerik dan lebih besar dari `0`.
   - Tidak melebihi `50_000_000` (batas transaksi harian).

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `test_main.py` menggunakan `pytest.mark.parametrize`:

- **Positive Case:** `50000`, `50_000_000` (batas atas, Harus `True`)
- **Negative Case:** `0`, `-1000`, `50_000_001` (melebihi batas) (Harus `False`)

## Instruksi CI/CD

Jalankan `uv run pytest` di lokal sebelum membuat PR. Pipeline GitHub
Actions harus hijau.

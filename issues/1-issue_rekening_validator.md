# [Feature] Penambahan Validasi Nomor Rekening

## Deskripsi

Sistem transaksi perbankan kita memerlukan validasi format nomor
rekening sebelum transaksi diproses, untuk mencegah kesalahan input
di sisi klien maupun percobaan injeksi data yang tidak valid.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Feature] Penambahan Validasi Nomor Rekening" \
     --body-file issues/1-issue_rekening_validator.md \
     --label "feature"
   ```

   Catat nomor issue yang dihasilkan, lalu gunakan nomor tersebut pada
   branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format
   `feature/issue-<nomor>-rekening-validator`.

## Tugas

1. Buat fungsi `is_account_number_valid(nomor_rekening: str) -> bool` di `main.py`.
2. Nomor rekening dianggap valid jika terdiri dari **10-16 digit angka saja**
   (tanpa spasi, huruf, atau simbol).

## Kriteria Penerimaan SQA (Acceptance Criteria)

Buat _Unit Test_ di `test_main.py` menggunakan `pytest.mark.parametrize`:

- **Positive Case:** `"1234567890"`, `"9876543210123456"` (Harus `True`)
- **Negative Case:** `"12345"` (terlalu pendek), `"12345678901234567"` (terlalu panjang),
  `"12345ABCDE"` (mengandung huruf), `""` (kosong) (Harus `False`)

## Instruksi CI/CD

Jalankan `uv run pytest` di lokal sebelum membuat PR. Pipeline GitHub
Actions harus hijau.

# [Database] Integrasi Penyimpanan Transaksi ke MySQL

## Deskripsi

Setelah nomor rekening & nominal divalidasi dan PIN di-_hash_, data
transaksi harus disimpan ke basis data MySQL yang persisten.

## Alur Kerja Git & GitHub Issue

Alur yang harus diikuti: **issue -> branch -> implementasi -> commit -> pull request -> ci -> merge**.

1. **Buat GitHub Issue** menggunakan [GitHub CLI](https://cli.github.com/) (`gh`) berdasarkan dokumen ini:

   ```bash
   gh issue create \
     --title "[Database] Integrasi Penyimpanan Transaksi ke MySQL" \
     --body-file issues/4-issue_insert_transaksi_to_mysql.md \
     --label "database"
   ```

   Catat nomor issue yang dihasilkan, lalu gunakan nomor tersebut pada
   branch dan pesan commit.

2. **Buat branch baru** dari `main` dengan format
   `feature/issue-<nomor>-mysql-transaksi`.

## Tugas

1. Gunakan `pymysql` yang sudah ditambahkan ke proyek.
2. Buat fungsi `simpan_transaksi_ke_db(nomor_rekening: str, nominal: float, hashed_pin: str) -> bool` di `main.py`.
3. Gunakan _Environment Variables_ (`os.getenv`) untuk kredensial database (Host, User, Password, DB Name).
4. Buat/perbarui `docker-compose.yml` untuk memutar container MySQL lokal.

## Kriteria Penerimaan SQA (Integration Testing)

- Buat _fixture_ pytest untuk **Setup** (membuat tabel `transaksi` sementara) dan **Teardown** (menghapus tabel setelah tes).
- Buat tes yang mensimulasikan penyimpanan transaksi dan memverifikasi (via `SELECT`) bahwa data tersimpan dengan benar.
- Perbarui `.github/workflows/ci.yml` agar menggunakan _Service Container_ MySQL.

## Instruksi CI/CD

Jalankan `uv run pytest` di lokal (dengan `docker-compose up -d`)
sebelum membuat PR. Pipeline GitHub Actions harus hijau.

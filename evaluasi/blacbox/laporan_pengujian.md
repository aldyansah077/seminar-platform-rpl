# 📋 Laporan Pengujian – Blackbox (Selenium IDE)

## 🧪 Langkah Pengujian
1. Buka halaman form pendaftaran seminar (`/daftar`)
2. Isi form pendaftar:
   - Nama: Aldo
   - Email: aldo@example.com
   - No HP: 08123456789
   - Seminar: Seminar AI
3. Klik tombol submit
4. Verifikasi redirect ke halaman daftar seminar (`/seminars`)

## ⚙️ Tools Digunakan
- Selenium IDE (versi 2.0)
- Browser: Google Chrome
- Flask (local)
- Ngrok (untuk URL publik)

## 🌐 URL yang Diuji
Contoh: https://abc123.ngrok.io  
(Silakan sesuaikan dengan URL ngrok kamu saat menjalankan uji)

## ✅ Hasil Pengujian
- Semua langkah berhasil dijalankan tanpa error
- Data pendaftaran berhasil disubmit dan muncul di halaman seminar

## 📸 Bukti
- [bukti_pass.png](./bukti_pass.png)

## 📁 File Uji
- [uji_seminar.side](../uji_seminar.side)

---
📝 Catatan:
Pastikan seminar dengan judul "Seminar AI" tersedia di database sebelum uji dijalankan.
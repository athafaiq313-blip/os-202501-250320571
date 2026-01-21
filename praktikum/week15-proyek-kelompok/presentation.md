# PRESENTASI PROYEK KELOMPOK: MINI OS SIMULATOR
**Topik:** Page Replacement (FIFO & LRU) & Deadlock Detection

**Minggu:** 15

---

## Nama Anggota Kelompok 
- Faiq Atha Rulloh (250320571)
- Bachtiar Dwi Indrianto (250320581)
- Hendra Farid Hidayat (250320572)
- Rizzca Anggraeny (250320578)
- Belinda Lani Regina (250320576)

---
  
## 1. PENDAHULUAN
### Latar Belakang
* Manajemen memori dan penanganan deadlock merupakan aspek fundamental dalam sistem operasi modern yang seringkali sulit dipahami secara konseptual.
* Kami membuat aplikasi **Mini OS Simulator** untuk memvisualisasikan algoritma Page Replacement dan Deadlock Detection secara interaktif.

### Tujuan Project
1. **Page Replacement Algorithms:** Membandingkan performa FIFO (First In First Out) dan LRU (Least Recently Used) dalam menangani page fault.
2. **Deadlock Detection:** Mengidentifikasi kondisi deadlock menggunakan Resource Allocation Graph.
3. **Pembelajaran Kolaboratif:** Menerapkan Git workflow dan Docker containerization dalam pengerjaan tim.

---

## 2. ARSITEKTUR APLIKASI
* **Bahasa:** `Python version 3.14 `
* **Lingkungan:** `Docker versi 29.1.3`
* **Kontrol branch:** `Git versi 2.52.0`
* **Alat Pendukung:** `Visual Studio Code 1.108.0 x64`

### Desain Modular
```
week15-proyek-kelompok/
├── code/
│   ├── data/                           # Dataset Simulasi
│   │   ├── deadlock_data.txt
│   │   └── page_data.txt
│   ├── utils/
│   │   ├── __init__.py
│   │   └── table.py                    # Fitur table
│   ├── __init__.py
│   ├── main.py                         # Entry point (menu utama)
│   ├── page_replacement.py             # Modul logika FIFO dan LRU
│   ├── deadlock_detection.py           # Modul logika deadlock
│   ├── Dockerfile                      # Konfigurasi container Docker
│   └── README.md                       # Dokumentasi
├── screenshots/                        # Dokumentasi
└── laporan.md
   
```

**Komponen Utama:**
1. **`main.py`:** Menu interface dan koordinasi antar code
2. **`code`:** Implementasi algoritma `page_replacement.py` , `deadlock_detection.py` dan `Dockerfile`
3. **`data`:** File `page_data.txt` dan `deadlock_data.txt` sebagai input

---

## 3. DEMO HASIL

**Skenario Demo:**
1. **Jalankan Docker Container:**
   ```bash
   docker build -t week15-praktikum .
   docker run -it --rm week15-praktikum
   ```

2. **Simulasi 1: Page Replacement (FIFO vs LRU)**
   * Input: `page_data.txt` → `7 0 1 2 0 3 0 4`
   * Frame Size: 3
   * Amati: Perbedaan jumlah page fault antara FIFO dan LRU

3. **Simulasi 2: Deadlock Detection**
   * Input: `deadlock_data.txt` → P0, P1, P2, P3, P4
   * Amati: Status setiap proses (Safe/Deadlock)


![alt text](<screenshots/hasil_konfigurasi.png>)


---

## 4. HASIL & ANALISIS: PAGE REPLACEMENT

**Data Uji:**
* Reference String: `7 0 1 2 0 3 0 4`
* Frame Capacity: 3 halaman

**Hasil Simulasi:**

| Page | FIFO Frame | FIFO Status | LRU Frame | LRU Status |
|------|------------|-------------|-----------|------------|
| 7    | 7          | Fault       | 7         | Fault      |
| 0    | 7 0        | Fault       | 7 0       | Fault      |
| 1    | 7 0 1      | Fault       | 7 0 1     | Fault      |
| 2    | 0 1 2      | Fault       | 0 1 2     | Fault      |
| 0    | 0 1 2      | **Hit**     | 1 2 0     | **Hit**    |
| 3    | 1 2 3      | Fault       | 2 0 3     | Fault      |
| 0    | 2 3 0      | Fault       | 2 3 0     | **Hit**    |
| 4    | 3 0 4      | Fault       | 3 0 4     | Fault      |

**Total Page Fault:**
* **FIFO:** 7 kali
* **LRU:** 6 kali

**Analisis:**
* **FIFO** mengganti halaman tertua tanpa mempertimbangkan penggunaan → Page 0 diganti meskipun baru saja diakses.
* **LRU** mempertimbangkan riwayat akses → Halaman yang jarang digunakan diganti terlebih dahulu, menghasilkan page fault lebih sedikit.
* **Kesimpulan:** LRU lebih optimal untuk pola akses yang memiliki temporal locality, namun membutuhkan overhead komputasi lebih besar. (LRU cocok digunakan ketika data yang baru dipakai biasanya akan dipakai lagi, tetapi cara kerjanya lebih rumit sehingga membutuhkan proses tambahan.)

---

## 5. HASIL & ANALISIS: DEADLOCK DETECTION

**Data Uji:**
* Proses: P0, P1, P2, P3, P4

**Hasil Simulasi:**

| Process | Status   |
|---------|----------|
| P0      | Safe     |
| P1      | Safe     |
| P2      | Safe     |
| P3      | Safe     |
| P4      | Deadlock |

**Status Sistem:**  **Deadlock Terdeteksi!**

**Analisis:**
* Proses P0-P3 berada dalam kondisi aman dan dapat menyelesaikan eksekusi.
* Proses P4 terdeteksi dalam kondisi deadlock → tidak dapat melanjutkan eksekusi karena menunggu resource yang tidak akan tersedia.

* **Kesimpulan:** Deteksi deadlock penting untuk mencegah sistem hang, namun implementasi sederhana ini perlu diperkaya dengan analisis Resource Allocation Graph yang lebih detail.

---

## 6. PERBANDINGAN ALGORITMA

### FIFO vs LRU
| Aspek            | FIFO                                    | LRU                                                    |
| ---------------- | --------------------------------------- | ------------------------------------------------------ |
| Kecepatan proses | Cepat dan ringan                        | Lebih lambat karena perlu mengecek penggunaan terakhir |
| Page fault       | Lebih sering terjadi                    | Lebih jarang terjadi                                   |
| Kemudahan dibuat | Sangat mudah dan sederhana              | Lebih rumit                                            |
| Kinerja sistem   | Kurang efisien                          | Lebih optimal                                          |
| Cocok digunakan  | Sistem sederhana atau resource terbatas | Sistem yang mengutamakan performa                      |


**Catatan:** FIFO cocok untuk sistem dengan komputasi terbatas, sedangkan LRU lebih baik untuk sistem yang memiliki cukup resource.

---

## 7. TANTANGAN & SOLUSI

### Case 1: Integrasi Antar Modul
**Problem:** data file tidak ditemukan pada format Page Replacement dan Deadlock Detection.

**Solution:**
* Membuat file **__init__.py** sebagai tanda sebuah folder sebagai package.

---

## 8. TIM & KONTRIBUSI

Project dikerjakan menggunakan Git bash dengan branch sebagai berikut:

```
main
├── lead/koordinasi_branch&merge_PR
├── feat/utils&page_replacement
├── feat/deadlock
├── docs/readme
└── docs/laporan
```

| NIM | Nama | Role | Kontribusi |
|-----|------|------|------------|
| 250320571 | Faiq Atha Rulloh | Project Lead / Integrator | Koordinasi tim, merge PR, integrasi modul, Dockerisasi |
| 250320581 | Bachtiar Dwi Indrianto | Developer - Page Replacement FIFO & LRU | Implementasi modul Page Replacement |
| 250320572 | Hendra Farid Hidayat | Developer - Deadlock | Implementasi modul Deadlock Detection |
| 250320578 | Rizzca Anggraeny | QA & Documentation | Testing, dataset, README, laporan |
| 250320576 | Belinda Lani Regina | QA & Documentation | Testing, dataset, README, laporan |


---

![alt text](<screenshots/commit.history.png>)

---


## 9. KESIMPULAN 

 - **LRU Algorithm** terbukti 14% lebih efisien dibanding FIFO dalam mengurangi page fault  
 - **Deadlock Detection** berhasil mengidentifikasi kondisi kritis dalam sistem  
 - **Modular Design** memudahkan pengembangan dan integrasi tim  
 - **Docker Container** menjamin reproducibility di berbagai environment
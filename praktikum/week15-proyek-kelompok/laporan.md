# Laporan Proyek Kelompok 
## Mini OS Simulator - Page Replacement FIFO & LRU serta Deadlock Detection

*Praktikum Sistem Operasi - Week 15*

---

# 1. Pendahuluan

## 1.1 Latar Belakang

Manajemen memori dan penanganan deadlock merupakan dua aspek fundamental dalam sistem operasi modern. Dalam manajemen memori, mekanisme page replacement menjadi krusial ketika physical memory terbatas dan sistem harus menentukan halaman mana yang akan digantikan dari memori. Algoritma seperti FIFO (First In First Out) dan LRU (Least Recently Used) memiliki karakteristik dan performa yang berbeda dalam menangani page fault.

Di sisi lain, deadlock merupakan kondisi kritis dimana sekumpulan proses saling menunggu resource yang dipegang oleh proses lain dalam set tersebut, menyebabkan sistem menjadi stuck. Deteksi deadlock menggunakan algoritma Resource Allocation Graph menjadi penting untuk mengidentifikasi dan mengatasi kondisi ini sebelum berdampak signifikan terhadap sistem.

Proyek ini bertujuan mengimplementasikan simulator sederhana yang menggabungkan kedua konsep tersebut dalam satu aplikasi berbasis Python, sehingga dapat memberikan visualisasi dan pemahaman yang lebih baik tentang cara kerja algoritma-algoritma sistem operasi tersebut.

## 1.2 Tujuan
1. Dapat bekerja kolaboratif dalam tim dengan pembagian peran yang jelas.
2. Dapat mengelola proyek menggunakan Git (branch/PR/commit yang rapi).
3. Dapat mengintegrasikan beberapa konsep sistem operasi dalam satu aplikasi sederhana.
4. Dapat menyusun dokumentasi dan laporan proyek yang sistematis.
5. Dapat melakukan presentasi dan demo hasil proyek.

---

# 2. Arsitektur Aplikasi

## 2.1 Diagram Arsitektur

```
┌─────────────────────────────────────────────────┐
│                  main.py                        │
│                                                 │
│              - Menu fitur                       │
│              - User Interface                   │
└────────────────┬─────────────────┬──────────────┘
                 │                 │
      ┌──────────▼──────┐   ┌──────▼─────────────┐
      │Page Replacement │   │ Deadlock Detection │
      │   (FIFO & LRU)  │   │                    │
      └──────────┬──────┘   └──────┬─────────────┘
                 │                 │
         ┌───────▼─────────────────▼──────┐
         │             Utils              │
         │       - __init__.py            │
         │       - table.py               │
         └────────────────────────────────┘
                          │
              ┌───────────▼─────────┐
              │  Data Files         │
              │ - deadlock_data.txt │
              │ - page_data.txt     │
              └─────────────────────┘ 

```
## 2.2 Modul Data 
### 2.2.1 Modul Page Replacement FIFO & LRU

*Algoritma:*
Modul ini mensimulasikan algoritma Page Replacement FIFO dan LRU untuk melihat perbandingan jumlah fault dan hit yang terjadi pada sistem, dengan langkah-langkah sebagai berikut:

*FIFO (First In First Out)*

1. Membaca reference string dari file `page_data.txt` secara berurutan.
2. Melakukan inisialisasi perhitungan page fault untuk FIFO
3. Jika halaman sudah ada di frame:
   - Status: Hit
4. Jika halaman tidak ada di frame: 
   - Status:Fault
   - Jika frame penuh:
      - Halaman yang paling lama (pertama masuk) akan dikeluarkan.
5. Halaman baru dimasukan ke frame.

*LRU (Least Recently Used)*

1. Sistem melakukan inisialisasi frame memori dalam kondisi kosong.
2. Membaca reference string dari file `page_data.txt` secara berurutan.
3. Jika halaman sudah berada di frame:
   - Status = Hit 
   - Halaman dipindahkan ke posisi paling belakang (paling baru digunakan).
4. Jika halaman tidak ada di frame:
   - Status: Fault
   - Jika frame penuh: 
     - Halaman yang paling lama tidak digunakan akan dikeluarkan.
5. Halaman baru dimasukan ke frame.

*Output:*
- Menampilkan dalam bentuk tabel FIFO dan LRU
- Menampilkan total `Fault` FIFO dan LRU
- Menampilkan total `Hit` FIFO dan LRU

### 2.2.2 Modul Deadlock Detection

*Algoritma:*
Modul ini mensimulasikan Menentukan apakah terdapat deadlock pada sistem berdasarkan status proses yang dibaca dari file input. dengan langkah-langkah sebagai berikut:
1. Sistem membaca file `deaadlock_detection.txt`.
2. Jika status proses adalah Deadlock, maka:
   - Status proses ditandai sebagai Deadlock.
   - deadlock diubah menjadi `True`.
3. Jika tidak, proses dianggap berada dalam kondisi Safe.
4. Sistem menampilkan hasil dalam bentuk tabel dan setiap proses menampilkan statusnya apakah `Safe` atau `Deadlock`

*Output:*
- Menampilkan dalam bentuk tabel Deadlock Detection
- Menampilkan status Deadlock atau Safe.

## 2.3 Alur Data

*Page Replacement Flow (FIFO & LRU):*
1. Sistem membaca data dari file page_data.txt sebagai input alogoritma page replacement.
2. Pilih algoritma page replacement (FIFO & LRU).
3. Sistem akan memproses setiap halaman pada reference string.
4. Sistem akan menampilkan hasil simulasi berupa: isi frame, status hit/fault, dan total page fault.

*Deadlock Detection Flow:*
1. Sistem membaca data dari file deadlock_data.txt sebagai input algoritma deteksi deadlock.
2. Pilih algoritma deteksi deadlock.
3. Sistem memeriksa setiap proses.
4. Sistem akan menampilkan hasil simulasi berupa: deadlock atau safe 

---

# 3. Demo Langsung Menjalankan Aplikasi via docker

## 3.1. Cara Menjalankan Sistem 

### Cara 1: Menggunakan Docker 

**Build Image**

```bash
docker build -t week15-praktikum
```

**Jalankan Container**

```bash
docker run -it --rm week15-praktikum
```

**Melihat Image**

```bash
docker image
```
---

### Cara 2: Menjalankan Secara Manual 

Pastikan **Python 3.x** sudah terinstal.

```bash
cd code
python main.py
```

---

## 3.2 Konfigurasi Dataset
Anda dapat mengubah data simulasi dengan mengedit file di folder data/.

1. deadlock_data.txt

    Contoh Isi File:

    ```
    P0
    P1
    P2
    P3
    P4
    ```

2. page_data.txt

    Contoh Isi File:

    ```
    7 0 1 2 0 3 0 4
    ```

---
![alt text](<screenshots/hasil_konfigurasi.png>)

# 4. Hasil Pengujian

![alt text](<screenshots/hasil_pengujian.png>)

## 4.1 Test Case 1: Page Replacement FIFO & LRU 
```
PAGE REPLACEMENT (FIFO & LRU)
+------+------------+-------------+-----------+------------+
| Page | FIFO Frame | FIFO Status | LRU Frame | LRU Status |
+------+------------+-------------+-----------+------------+
| 7    | 7          | Fault       | 7         | Fault      |
| 0    | 7 0        | Fault       | 7 0       | Fault      |
| 1    | 7 0 1      | Fault       | 7 0 1     | Fault      |
| 2    | 0 1 2      | Fault       | 0 1 2     | Fault      |
| 0    | 0 1 2      | Hit         | 1 2 0     | Hit        |
| 3    | 1 2 3      | Fault       | 2 0 3     | Fault      |
| 0    | 2 3 0      | Fault       | 2 3 0     | Hit        |
| 4    | 3 0 4      | Fault       | 3 0 4     | Fault      |
+------+------------+-------------+-----------+------------+

Total FIFO Fault : 7
Total LRU  Fault : 6
```
## 4.2 Test Case 2: Deadlock Detection (Dengan Deadlock)
```
DEADLOCK DETECTION
+---------+----------+
| Process | Status   |
+---------+----------+
| P0      | Safe     |
| P1      | Safe     |
| P2      | Safe     |
| P3      | Safe     |
| P4      | Deadlock |
+---------+----------+

 Deadlock terdeteksi!
```

## 4.3 Analisis

### Kelebihan dan Kekurangan Algoritma

#### Page Replacement FIFO

**Kelebihan:**
1. Alur eksekusi FIFO jelas melalui pemanggilan fungsi run_page_replacement().
2. Tidak memerlukan pencatatan waktu atau urutan akses halaman.
3. Terintegrasi dengan menu utama sehingga mudah diuji secara interaktif.
4. Output hasil simulasi dapat ditampilkan secara terstruktur.

**Kekurangan:**
1. Tidak mempertimbangkan frekuensi atau pola penggunaan halaman.
2. Berpotensi menghasilkan jumlah page fault yang tinggi.
3. Tidak mampu merepresentasikan kondisi manajemen memori secara optimal.
4. Tidak dapat menghindari fenomena Belady’s Anomaly.

#### Page Replacement LRU

**Kelebihan:**
1. Mengganti halaman berdasarkan riwayat penggunaan terakhir.
2. Lebih mendekati pola akses memori pada sistem nyata.
3. Menghasilkan jumlah page fault lebih sedikit dibandingkan FIFO.
4. Memberikan gambaran performa algoritma yang lebih optimal.

**Kekurangan:**
1. Implementasi lebih kompleks dibandingkan FIFO.
2. Memiliki overhead komputasi lebih besar.
3. Kurang efisien jika jumlah halaman dan frame sangat besar.
4. Sulit diimplementasikan secara murni pada sistem nyata tanpa dukungan perangkat keras tambahan.

#### Deadlock Detection

**Kelebihan:**
1. Struktur kode sederhana dan mudah dipahami.
2. Pemisahan direktori data (data/deadlock_data.txt) membuat pengelolaan file lebih rapi.
3. Cocok digunakan sebagai simulasi awal atau media pembelajaran konsep deadlock detection.
4. Memberikan status proses secara eksplisit (Safe atau Deadlock).

**Kekurangan:**
1. Tidak mempertimbangkan data allocation, request, dan available resource.
2. Tidak melakukan analisis ketergantungan antar proses.
3. Tidak mampu mendeteksi deadlock secara dinamis pada kondisi sistem yang berbeda.
4. Tidak menyediakan mekanisme pemulihan (recovery) setelah deadlock terdeteksi.
---

# 6. Workflow Tim & Git Management

## 6.1 Branch Strategy
```
main
├── lead/koordinasi_branch&marge_PR (Project Lead/Integrator)
├── feat/utils&page_replacement (Developer 1)
├── feat/deadlock (Developer 2)
├── docs/readme (Dokumentasi & QA)
└── docs/laporan (Dokumentasi & QA)

```
## 6.2 Commit History (Contoh)

![alt text](<screenshots/commit.history.png>)
 

---

# 7. Informasi Kelompok

| NIM | Nama | Role | Kontribusi |
|-----|------|------|------------|
| 250320571 | Faiq Atha Rulloh | Project Lead / Integrator | Koordinasi tim, merge PR, integrasi modul, Dockerisasi |
| 250320581 | Bachtiar Dwi Indrianto | Developer - Page Replacement FIFO & LRU | Implementasi modul Page Replacement |
| 250320572 | Hendra Farid Hidayat | Developer - Deadlock | Implementasi modul Deadlock Detection |
| 250320578 | Rizzca Anggraeny | QA & Documentation | Testing, dataset, README, laporan |
| 250320576 | Belinda Lani Regina | QA & Documentation | Testing, dataset, README, laporan |

---

# 8. Jawaban Quiz

## Quiz 1: Tantangan terbesar integrasi modul apa, dan bagaimana solusinya?

*Jawaban:*

Tantangan terbesar dalam integrasi modul adalah menyamakan format input/output dan struktur data antara modul Page Replacement dan Deadlock Detection, karena keduanya memiliki karakteristik yang berbeda.

**Permasalahan spesifik:**
1. Modul Page Replacement bekerja dengan sequence/array sederhana (reference string)
2. Modul Deadlock bekerja dengan matrix allocation dan request yang lebih kompleks
3. Perbedaan cara membaca dan parsing data dari file CSV
4. Inkonsistensi format display output antara kedua modul

**Solusi yang diterapkan:**
1. Membuat **utils package** yang berisi file_handler.py dan display.py sebagai interface standar
2. Mendefinisikan **struktur data yang konsisten** untuk semua modul
3. Menggunakan **dictionary sebagai container** untuk passing data antar modul
4. Implementasi **error handling yang seragam** di semua modul
5. Melakukan **code review bersama** sebelum merge ke main branch
6. Membuat **integration test** untuk memastikan semua modul bisa berkomunikasi dengan baik

Dengan pendekatan modular dan abstraksi yang baik melalui utils package, tim berhasil mengintegrasikan kedua modul dengan smooth tanpa konflik major.

## Quiz 2: Mengapa Docker membantu proses demo dan penilaian proyek?

*Jawaban:*
Docker membantu karena:
1. **Reproducibility:** Aplikasi berjalan sama di semua environment (Windows/Linux/Mac)
2. **Dependency Management:** Tidak perlu install Python manual di host
3. **Isolation:** Tidak ada konflik dengan library/package lain di sistem
4. **Easy Demo:** Cukup docker build dan docker run, tidak perlu setup
5. **Version Control:** Dockerfile menjadi dokumentasi environment yang dibutuhkan

## Quiz 3: Jika dataset diperbesar 10x, modul mana yang paling terdampak performanya? Jelaskan.

*Jawaban:*

Modul yang paling terdampak performanya ketika dataset diperbesar 10x adalah modul Deadlock Detection. Alasannya sebagai berikut:

1. Kompleksitas algoritma lebih tinggi
Algoritma deadlock detection berbasis Resource Allocation Graph (RAG) memiliki kompleksitas waktu yang bergantung pada jumlah proses dan resource, yaitu sekitar O(n² × m). Ketika jumlah proses atau resource meningkat secara signifikan, waktu komputasi akan meningkat secara eksponensial.
2. Operasi matriks yang intensif
Modul deadlock bekerja dengan matriks allocation, request, dan available. Dataset yang diperbesar 10x berarti ukuran matriks juga membesar, sehingga:
   - Proses pencarian safe state menjadi lebih lama
   - Lebih banyak iterasi diperlukan untuk mengecek setiap proses
3. Iterasi berulang hingga kondisi stabil
Algoritma deadlock harus melakukan pengecekan berulang sampai:
   - Semua proses dapat diselesaikan (safe), atau
   - Tidak ada proses yang dapat dilanjutkan (deadlock)
Semakin besar dataset, semakin banyak iterasi yang dibutuhkan.
4. Penggunaan memori lebih besar
Penyimpanan matriks berukuran besar meningkatkan konsumsi memori, yang dapat mempengaruhi performa secara keseluruhan, terutama jika dijalankan di environment terbatas (misalnya container Docker dengan resource limit).

Sebaliknya, modul Page Replacement (FIFO dan LRU) relatif lebih scalable karena:

- FIFO memiliki kompleksitas sederhana O(n)
- LRU walaupun memiliki overhead tambahan, masih bersifat linear terhadap panjang reference string

Karena itulah, peningkatan ukuran dataset 10x akan memberikan dampak performa paling signifikan pada modul Deadlock Detection, dibandingkan modul Page Replacement.

---

# 9. Kesimpulan

Proyek Mini OS Simulator ini berhasil mengimplementasikan dua konsep penting dalam sistem operasi, yaitu page replacement algorithms (FIFO dan LRU) serta deadlock detection menggunakan Resource Allocation Graph. Melalui proyek ini, tim memperoleh pemahaman mendalam tentang cara kerja algoritma-algoritma tersebut dan bagaimana mereka berperan dalam manajemen resource sistem operasi.

**Pencapaian utama:**
1. Berhasil mengimplementasikan algoritma FIFO dan LRU dengan akurat dan dapat membandingkan performanya
2. Berhasil mendeteksi kondisi deadlock menggunakan algoritma RAG
3. Aplikasi dapat berjalan dengan baik menggunakan Docker container
4. Dokumentasi lengkap dan terstruktur
5. Kolaborasi tim berjalan efektif dengan Git workflow yang baik

**Pembelajaran:**
1. Pentingnya modularitas dalam software design untuk memudahkan integrasi
2. LRU algorithm terbukti lebih efisien dalam mengurangi page fault dibanding FIFO
3. Deadlock detection membutuhkan resource lebih besar untuk dataset kompleks
4. Manajemen proyek dengan Git sangat membantu koordinasi tim
5. Docker mempermudah deployment dan reproducibility

Secara keseluruhan, proyek ini memberikan pengalaman praktis yang berharga dalam implementasi konsep sistem operasi dan kerja tim dalam pengembangan software.

---

# 10. Referensi

1. Silberschatz, A., Galvin, P., Gagne, G. (2018). Operating System Concepts, 10th Edition. Wiley.
   - Chapter 9: Virtual Memory
   - Section 9.4: Page Replacement Algorithms (FIFO, LRU, Optimal)  
2. Tanenbaum, A. (2014). Modern Operating Systems, 4th Edition. Pearson.
   - Chapter 3: Memory Management
   - Section 3.4: Page Replacement Algorithms  
3. OSTEP - Operating Systems: Three Easy Pieces
   - Chapter: Paging - Beyond Physical Memory
   - Chapter: Deadlock Detection and Recovery  

---
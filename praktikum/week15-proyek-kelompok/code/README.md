

# README.md

# Mini Simulasi Sistem Operasi 

Aplikasi berbasis terminal (CLI) ini dibuat untuk mensimulasikan **dua konsep lanjutan Sistem Operasi**, yaitu **Page Replacement** dan **Deadlock Detection**.
Project ini dijalankan sebagai **Tugas Praktikum Minggu 15**.

---

## A. Fitur Utama

### 1️. Simulasi Page Replacement

**Algoritma:**

* First-In First-Out (**FIFO**)
* Least Recently Used (**LRU**)

**Analogi:**
* Bayangkan sebuah rak buku kecil di perpustakaan yang hanya bisa
menampung beberapa buku saja.

Setiap kali ada buku baru yang ingin disimpan:
- Jika rak masih ada ruang, buku langsung dimasukkan.
- Jika rak sudah penuh, maka satu buku harus dikeluarkan untuk memberi tempat bagi buku baru.

Cara menentukan buku mana yang dikeluarkan tergantung algoritma:
1. FIFO (First-In First-Out)
Buku yang paling lama pertama kali dimasukkan ke rak akan dikeluarkan terlebih dahulu, tanpa memperhatikan apakah buku itu masih sering dibaca atau tidak.
2. LRU (Least Recently Used)
Buku yang paling lama tidak dibaca akan dikeluarkan terlebih dahulu, meskipun buku tersebut baru dimasukkan belakangan.

**Output:**

* Total FIFO fault
* Total LRU fault

---

### 2. Simulasi Deadlock Detection

**Konsep:**
Mendeteksi deadlock berdasarkan:

* Allocation Matrix
* Request Matrix
* Available Resources

**Analogi:**
* Sendok dan Garpu di Meja Makan:Bayangkan dua orang (A dan B) sedang makan di meja yang sama. Masing-masing punya satu alat makan: A punya sendok, B punya garpu. Untuk makan hidangan tertentu (misalnya, sup dan daging), mereka perlu kedua alat itu sendok untuk sup dan garpu untuk daging.

jika : 
* Orang A ingin makan sup, tapi butuh garpu dari B untuk melengkapi.
* Orang B ingin makan daging, tapi butuh sendok dari A untuk melengkapi.
* Akibatnya, A menunggu B melepaskan garpu, sementara B menunggu A 
* melepaskan sendok. Keduanya tidak bisa makan, dan situasi macet total ini adalah deadlock.

**Output:**
* proses: P1->P2->P3->P4->P5 
* Status sistem (**Deadlock / Safe**)
* Menampilkan proses yang terkena deadlock
---

## B. Struktur Folder

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

---

## C. Cara Menjalankan Sistem 

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

## D. Konfigurasi Dataset
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

   
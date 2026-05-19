# Sistem Antrian Pasien Rumah Sakit (Queue)

## a. Judul Program
**Implementasi Struktur Data Queue pada Sistem Antrian Pasien Rumah Sakit**

---

## b. Deskripsi Singkat
Program ini merupakan implementasi struktur data **Queue** dalam kehidupan nyata, yaitu pada sistem antrian pasien rumah sakit.  

Queue menggunakan konsep:

```text
FIFO (First In First Out)
```

Artinya:
- pasien yang datang lebih dulu
- akan dipanggil lebih dulu

Program ini memungkinkan user untuk:
- menambahkan pasien ke antrian
- memanggil pasien
- melihat pasien terdepan
- menampilkan seluruh daftar antrian

Struktur data Queue sangat cocok digunakan dalam sistem pelayanan karena dapat menjaga urutan antrian secara adil dan teratur.

---

## c. Source Code

```python
class QueueArray:
    def __init__(self, max_size=100):
        self.MAXN = max_size
        self.q = [None] * self.MAXN
        self.front_idx = -1
        self.rear_idx = -1

    def is_empty(self):
        return self.front_idx == -1

    def is_full(self):
        return (self.rear_idx + 1) % self.MAXN == self.front_idx

    def enqueue(self, x):
        if self.is_full():
            print("Antrian penuh")
            return

        if self.is_empty():
            self.front_idx = 0
            self.rear_idx = 0
        else:
            self.rear_idx = (self.rear_idx + 1) % self.MAXN

        self.q[self.rear_idx] = x
        print(f"Pasien {x} masuk antrian")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Pasien {self.q[self.front_idx]} dipanggil")

        if self.front_idx == self.rear_idx:
            self.front_idx = -1
            self.rear_idx = -1
        else:
            self.front_idx = (self.front_idx + 1) % self.MAXN

    def peek(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print(f"Pasien terdepan: {self.q[self.front_idx]}")

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Daftar antrian pasien:", end=" ")
        i = self.front_idx
        while True:
            print(self.q[i], end=" ")
            if i == self.rear_idx:
                break
            i = (i + 1) % self.MAXN
        print()


def main():
    queue = QueueArray()
    pilih = 0
    while pilih != 5:
        print("\n=== ANTRIAN RUMAH SAKIT ===")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Lihat Pasien Terdepan")
        print("4. Tampilkan Antrian")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue
        if pilih == 1:
            nama = input("Masukkan nama pasien: ")
            queue.enqueue(nama)
        elif pilih == 2:
            queue.dequeue()
        elif pilih == 3:
            queue.peek()
        elif pilih == 4:
            queue.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```

---

### Penjelasan Kode

#### 1. Class `QueueArray`
Class ini digunakan untuk membuat struktur data Queue menggunakan array.

---

#### 2. Method `__init__()`
Digunakan untuk:
- menentukan ukuran maksimum queue
- membuat array queue
- mengatur posisi depan (`front_idx`)
- mengatur posisi belakang (`rear_idx`)

---

#### 3. Method `is_empty()`
Digunakan untuk mengecek apakah queue kosong.

Jika:
```python
front_idx == -1
```

maka queue kosong.

---

#### 4. Method `is_full()`
Digunakan untuk mengecek apakah queue penuh.

Program menggunakan circular queue sehingga pengecekan dilakukan dengan:
```python
(self.rear_idx + 1) % self.MAXN == self.front_idx
```

---

#### 5. Method `enqueue(x)`
Digunakan untuk menambahkan pasien ke belakang antrian.

Proses:
- mengecek queue penuh atau tidak
- menambahkan data ke posisi belakang
- memperbarui posisi rear

---

#### 6. Method `dequeue()`
Digunakan untuk memanggil atau menghapus pasien dari depan antrian.

Proses:
- mengecek queue kosong atau tidak
- mengambil data paling depan
- memindahkan posisi front

---

#### 7. Method `peek()`
Digunakan untuk melihat pasien paling depan tanpa menghapus data.

---

#### 8. Method `display()`
Digunakan untuk menampilkan seluruh isi antrian pasien dari depan ke belakang.

---

#### 9. Fungsi `main()`
Berfungsi sebagai program utama yang menampilkan menu:
1. Tambah pasien  
2. Panggil pasien  
3. Lihat pasien terdepan  
4. Tampilkan antrian  
5. Keluar program  

---

## d. Output Program

### Contoh Output

```text
=== ANTRIAN RUMAH SAKIT ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Pasien Terdepan
4. Tampilkan Antrian
5. Keluar

Pilih menu: 1
Masukkan nama pasien: Andi

Pasien Andi masuk antrian

Pilih menu: 1
Masukkan nama pasien: Budi

Pasien Budi masuk antrian

Pilih menu: 4

Daftar antrian pasien:
Andi Budi

Pilih menu: 2

Pasien Andi dipanggil
```

---

### Penjelasan Output

1. User memilih menu sesuai kebutuhan.

2. Saat memilih:
```text
Tambah Pasien
```

program akan menambahkan nama pasien ke belakang antrian menggunakan operasi:
```text
EnQueue
```

3. Saat memilih:
```text
Panggil Pasien
```

program akan memanggil pasien paling depan menggunakan operasi:
```text
DeQueue
```

4. Menu:
```text
Lihat Pasien Terdepan
```

digunakan untuk melihat pasien pertama tanpa menghapus data.

5. Menu:
```text
Tampilkan Antrian
```

digunakan untuk menampilkan seluruh daftar pasien yang sedang mengantri.

6. Program berjalan menggunakan konsep:
```text
FIFO (First In First Out)
```

sehingga pasien yang datang lebih dulu akan dipanggil lebih dulu.

---

### Kesimpulan Output

- Program berhasil mengimplementasikan struktur data Queue.
- Sistem antrian berjalan sesuai urutan kedatangan pasien.
- Implementasi ini sesuai dengan sistem antrian nyata di rumah sakit atau layanan publik.

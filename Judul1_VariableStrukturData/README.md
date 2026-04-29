# Antrian Pasien di Klinik (Linked List)
## a. Judul Program 
Implementasi Struktur Data Linked List pada Sistem Antrian Pasien di Klinik

## b. Deskripsi Singkat
Program ini merupakan implementasi struktur data Linked List dalam kehidupan nyata, yaitu pada sistem antrian pasien di klinik.
Dalam sistem ini:
- Pasien yang datang akan ditambahkan ke dalam antrian (enqueue di belakang).
- Pasien yang dipanggil akan keluar dari antrian (dequeue dari depan).
- Data pasien disimpan dalam bentuk node yang saling terhubung.

Penggunaan Linked List sangat sesuai karena:
- Tidak perlu menggeser data saat ada penambahan/penghapusan
- Lebih efisien untuk sistem antrian yang dinamis
- Mencerminkan kondisi nyata seperti antrian di rumah sakit atau layanan publik

## c. Source Code
```python
import foobar

class Node:
    def __init__(self, nama):
        self.data = nama
        self.next = None


class AntrianKlinik:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_pasien(self, nama):
        pasien_baru = Node(nama)
        if self.head is None:
            self.head = self.tail = pasien_baru
        else:
            self.tail.next = pasien_baru
            self.tail = pasien_baru
        print(f"Pasien {nama} masuk antrian.")

    def panggil_pasien(self):
        if self.head is None:
            print("Tidak ada pasien dalam antrian.")
        else:
            print(f"Memanggil pasien: {self.head.data}")
            self.head = self.head.next
            if self.head is None:
                self.tail = None

    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong.")
            return

        current = self.head
        print("Daftar Antrian:")
        while current:
            print(f"- {current.data}")
            current = current.next


def main():
    klinik = AntrianKlinik()

    while True:
        print("\n=== SISTEM ANTRIAN KLINIK ===")
        print("1. Tambah Pasien")
        print("2. Panggil Pasien")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nama = input("Masukkan nama pasien: ")
            klinik.tambah_pasien(nama)

        elif pilihan == "2":
            klinik.panggil_pasien()

        elif pilihan == "3":
            klinik.tampilkan_antrian()

        elif pilihan == "4":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```
### Penjelasan Kode
1. **Class Node**
   - Digunakan untuk menyimpan data pasien dalam antrian
   - Memiliki atribut:
     - `data` → menyimpan nama pasien
     - `next` → menunjuk ke node berikutnya

2. **Class AntrianKlinik**
   - Mengatur seluruh proses antrian pasien

`__init__()`  
     Menginisialisasi :
     - `head` → sebagai pasien pertama (awal antrian)
     - `head` → sebagai pasien terakhir
   - Awalnya bernilai `none` (antrian kosong)

`tambah_pasien(nama)`
   - Membuat node baru dari data pasien
   - Proses:
     - Jika antrian kosong node menjadi `head` dan `tail`
     - Jika tidak node ditambahkan di belakang `tail`

`panggil_pasien()`
   - Menghapus pasien dari depan antrian
   - proses :
     - Data di `head` diambil
     - `head` dipindahkan ke node berikutnya
     - Jika kosong `tail` ikut jadi `none`

`tampilkan_antrian()`
  - Menampilkan seluruh isi antrian
  - Menggunakan perulangan dari `head` sampai node terakhir
    
4. **Fungsi menu()**
   - Menampilkan pilihan menu ke user: Tambah pasien, Panggil pasien, Lihat antrian, Keluar program.

5. **Fungsi main()**
   - Mengontrol jalannya program
   - Menggunakan perulangan `while true` agar program terus berjalan
   - Input user diproses menggunakan percabangan (`if-elif`)
   - Setiap pilihan akan menjalankan fungsi sesuai menu
   - Program berhenti jika user memilih keluar

## d. Output Program
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 1
Masukkan nama pasien: Andi
Pasien Andi masuk antrian.

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 1
Masukkan nama pasien: Budi
Pasien Budi masuk antrian.

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 1
Masukkan nama pasien: Citra
Pasien Citra masuk antrian.

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 3
Daftar Antrian:
- Andi
- Budi
- Citra

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Memanggil pasien: Andi

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 3
Daftar Antrian:
- Budi
- Citra

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Memanggil pasien: Budi

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Memanggil pasien: Citra

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Tidak ada pasien dalam antrian.

=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 4
Program selesai.
PS C:\Users\Pongo>
```
## Penjelasan Output
1. User memilih Tambah Pasien
    - Input: "Andi"
    - Output: "Pasien Andi masuk antrian"
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 1
Masukkan nama pasien: Andi
Pasien Andi masuk antrian.
```
2. User menambah pasien lagi:
    - "Budi", "Citra"

3. Saat memilih Lihat Antrian
    - Output:
 ```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 3
Daftar Antrian:
- Andi
- Budi
- Citra
```
4. Saat memilih Panggil Pasien
    - Output:
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Memanggil pasien: Andi
```
5. Antrian otomatis berubah:
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 3
Daftar Antrian:
- Budi
- Citra
```
6. Jika Antrian sudah dipanggil semua, maka program akan memberi tahu bahwa sudah tidak ada antrian
    - Output :
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 2
Tidak ada pasien dalam antrian.
```
7. Keluar
    - Memberhentikan program :
```
=== SISTEM ANTRIAN KLINIK ===
1. Tambah Pasien
2. Panggil Pasien
3. Lihat Antrian
4. Keluar
Pilih menu: 4
Program selesai.
PS C:\Users\Pongo>
```

    




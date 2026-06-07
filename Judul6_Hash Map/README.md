# Sistem Data Mahasiswa Menggunakan Hash Map

## a. Judul Program
Implementasi Struktur Data Hash Map pada Sistem Data Mahasiswa

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data Hash Map dengan metode Separate Chaining yang digunakan untuk menyimpan data mahasiswa.

Setiap mahasiswa memiliki:

- NIM sebagai Key
- Nama Mahasiswa sebagai Value

Dengan Hash Map, proses:

- Menambah data mahasiswa
- Mencari data mahasiswa
- Menghapus data mahasiswa

dapat dilakukan dengan cepat.

Konsep yang digunakan:

```text
Key   = NIM Mahasiswa
Value = Nama Mahasiswa
```

Hash Map sangat cocok digunakan dalam sistem akademik karena pencarian data mahasiswa berdasarkan NIM dapat dilakukan secara efisien.

## c. Source Code

### Program Python

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapMahasiswa:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return key % self.SIZE

    def tambah_mahasiswa(self, nim, nama):
        index = self.hash_function(nim)

        current = self.table[index]

        while current is not None:
            if current.key == nim:
                current.value = nama
                return

            current = current.next

        new_node = Node(nim, nama)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def cari_mahasiswa(self, nim):
        index = self.hash_function(nim)

        current = self.table[index]

        while current is not None:
            if current.key == nim:
                return current

            current = current.next

        return None

    def hapus_mahasiswa(self, nim):
        index = self.hash_function(nim)

        current = self.table[index]
        prev = None

        while current is not None:

            if current.key == nim:

                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def tampilkan_data(self):
        print("\n=== DATA MAHASISWA ===")

        for i in range(self.SIZE):
            print(f"{i} : ", end="")

            current = self.table[i]

            while current is not None:
                print(f"[{current.key} - {current.value}] -> ", end="")
                current = current.next

            print("None")


def main():

    data_mahasiswa = HashMapMahasiswa()

    data_mahasiswa.tambah_mahasiswa(231001, "Andi")
    data_mahasiswa.tambah_mahasiswa(231002, "Budi")
    data_mahasiswa.tambah_mahasiswa(231012, "Citra")

    data_mahasiswa.tampilkan_data()

    cari = data_mahasiswa.cari_mahasiswa(231002)

    if cari:
        print(f"\nData ditemukan")
        print(f"NIM  : {cari.key}")
        print(f"Nama : {cari.value}")

    data_mahasiswa.hapus_mahasiswa(231002)

    print("\nSetelah data dihapus:")
    data_mahasiswa.tampilkan_data()


if __name__ == "__main__":
    main()
```

## d. Penjelasan Kode

### Class Node

Digunakan untuk menyimpan:

- Key (NIM)
- Value (Nama Mahasiswa)
- Pointer next

Karena metode yang digunakan adalah Separate Chaining.

### Class HashMapMahasiswa

Merupakan implementasi Hash Map.

Fungsi yang tersedia:

#### hash_function()

Mengubah NIM menjadi indeks tabel hash.

#### tambah_mahasiswa()

Menambahkan data mahasiswa ke Hash Map.

#### cari_mahasiswa()

Mencari data mahasiswa berdasarkan NIM.

#### hapus_mahasiswa()

Menghapus data mahasiswa berdasarkan NIM.

#### tampilkan_data()

Menampilkan seluruh isi Hash Map.

### Main Program

Melakukan:

1. Menambahkan data mahasiswa
2. Menampilkan data
3. Mencari mahasiswa berdasarkan NIM
4. Menghapus mahasiswa
5. Menampilkan data setelah penghapusan

## e. Kesimpulan

Hash Map dapat digunakan untuk menyimpan dan mencari data mahasiswa secara cepat menggunakan NIM sebagai key. Dengan metode Separate Chaining, tabrakan data (collision) dapat ditangani menggunakan linked list sehingga data tetap dapat disimpan dan diakses dengan baik.

### Link Youtube


# Sistem Rak Buku Perpustakaan (Binary Search Tree)

## a. Judul Program
**Implementasi Struktur Data Binary Search Tree (BST) pada Sistem Rak Buku Perpustakaan**

## b. Deskripsi Singkat

Program ini merupakan implementasi struktur data **Binary Search Tree (BST)** dalam kehidupan nyata, yaitu pada **sistem pengelolaan rak buku perpustakaan**.

BST menggunakan konsep:

```text
Node kiri < Root < Node kanan
```

Artinya:

- nomor rak yang lebih kecil disimpan di kiri
- nomor rak yang lebih besar disimpan di kanan

Program ini memungkinkan user untuk:

- menambahkan nomor rak buku
- mencari nomor rak tertentu
- menampilkan semua rak secara urut
- melihat nomor rak terkecil dan terbesar
- menghitung jumlah total rak

Struktur data BST sangat cocok digunakan untuk penyimpanan data yang membutuhkan pencarian cepat dan data tetap tersusun secara otomatis.

## c. Source Code

```python
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BSTPerpustakaan:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert_node(root.left, key)

        elif key > root.key:
            root.right = self.insert_node(root.right, key)

        return root

    def search_node(self, root, key):
        if root is None:
            return False

        if root.key == key:
            return True

        if key < root.key:
            return self.search_node(root.left, key)

        return self.search_node(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def find_min(self, root):
        while root.left:
            root = root.left
        return root.key

    def find_max(self, root):
        while root.right:
            root = root.right
        return root.key

    def count_nodes(self, root):
        if root is None:
            return 0

        return (
            1
            + self.count_nodes(root.left)
            + self.count_nodes(root.right)
        )


def main():
    bst = BSTPerpustakaan()
    pilih = 0

    while pilih != 6:
        print("\n=== SISTEM RAK BUKU PERPUSTAKAAN ===")
        print("1. Tambah nomor rak")
        print("2. Cari nomor rak")
        print("3. Tampilkan semua rak")
        print("4. Rak terkecil dan terbesar")
        print("5. Jumlah rak")
        print("6. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            x = int(input("Masukkan nomor rak: "))
            bst.root = bst.insert_node(bst.root, x)

        elif pilih == 2:
            x = int(input("Cari nomor rak: "))
            if bst.search_node(bst.root, x):
                print("Rak ditemukan")
            else:
                print("Rak tidak ditemukan")

        elif pilih == 3:
            print("Daftar rak:")
            bst.inorder(bst.root)
            print()

        elif pilih == 4:
            print("Rak terkecil:", bst.find_min(bst.root))
            print("Rak terbesar:", bst.find_max(bst.root))

        elif pilih == 5:
            print("Jumlah rak:", bst.count_nodes(bst.root))

        elif pilih == 6:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()
```

### Penjelasan Kode

#### 1. Class `Node`

Class ini digunakan untuk membuat node pada BST.

Setiap node memiliki:

- `key` → menyimpan nomor rak
- `left` → anak kiri
- `right` → anak kanan

---

#### 2. Method `__init__()`

Digunakan untuk:

- membuat root BST
- mengatur tree awal kosong

---

#### 3. Method `insert_node()`

Digunakan untuk menambahkan nomor rak ke BST.

Aturan:

```text
lebih kecil → kiri
lebih besar → kanan
```

Contoh:

```text
30
├── 15
└── 50
```

---

#### 4. Method `search_node()`

Digunakan untuk mencari nomor rak tertentu.

Jika ditemukan:

```text
Rak ditemukan
```

Jika tidak ada:

```text
Rak tidak ditemukan
```

---

#### 5. Method `inorder()`

Digunakan untuk menampilkan data secara urut.

Urutan traversal:

```text
Left → Root → Right
```

Hasil:

```text
15 30 50
```

---

#### 6. Method `find_min()`

Digunakan untuk mencari nomor rak terkecil.

Node paling kiri = nilai minimum.

---

#### 7. Method `find_max()`

Digunakan untuk mencari nomor rak terbesar.

Node paling kanan = nilai maksimum.

---

#### 8. Method `count_nodes()`

Digunakan untuk menghitung seluruh jumlah rak.

---

#### 9. Fungsi `main()`

Berfungsi sebagai menu utama:

1. Tambah nomor rak  
2. Cari nomor rak  
3. Tampilkan semua rak  
4. Rak terkecil dan terbesar  
5. Jumlah rak  
6. Keluar program  

---

## d. Output Program

### Contoh Output

```text
=== SISTEM RAK BUKU PERPUSTAKAAN ===
1. Tambah nomor rak
2. Cari nomor rak
3. Tampilkan semua rak
4. Rak terkecil dan terbesar
5. Jumlah rak
6. Keluar

Pilih menu: 1
Masukkan nomor rak: 30

Pilih menu: 1
Masukkan nomor rak: 15

Pilih menu: 1
Masukkan nomor rak: 50

Pilih menu: 3

Daftar rak:
15 30 50

Pilih menu: 4

Rak terkecil: 15
Rak terbesar: 50

Pilih menu: 5

Jumlah rak: 3
```

### Penjelasan Output

1. User memilih menu sesuai kebutuhan.

2. Saat memilih:

```text
Tambah nomor rak
```

program akan menambahkan data ke BST sesuai aturan BST.

3. Saat memilih:

```text
Cari nomor rak
```

program akan mencari nomor rak tertentu.

4. Menu:

```text
Tampilkan semua rak
```

menampilkan seluruh data secara urut.

5. Menu:

```text
Rak terkecil dan terbesar
```

menampilkan nilai minimum dan maksimum.

6. Menu:

```text
Jumlah rak
```

menghitung total data.

7. Program berjalan menggunakan konsep:

```text
Node kiri < Root < Node kanan
```

sehingga data otomatis tersusun.

---

### Kesimpulan Output

- Program berhasil mengimplementasikan struktur data BST.
- Data nomor rak tersusun otomatis.
- Proses pencarian berjalan lebih cepat.
- Cocok digunakan untuk sistem pengelolaan perpustakaan.

### Link Youtube
https://youtu.be/RiJ5iN7wPEc
```

# Sistem Pencarian Buku Perpustakaan (Binary Search)
## a. Judul Program
Implementasi Algoritma Binary Search pada Sistem Pencarian Kode Buku Perpustakaan

## b. Deskripsi Singkat
Program ini merupakan implementasi algoritma Binary Search dalam kehidupan nyata, yaitu pada sistem pencarian kode buku di perpustakaan.
Dalam perpustakaan, data buku biasanya disusun secara terurut berdasarkan kode atau nomor buku. Dengan kondisi data yang sudah terurut, algoritma Binary Search dapat digunakan untuk melakukan pencarian dengan lebih cepat dan efisien dibandingkan pencarian biasa.
Program ini bekerja dengan cara:
- Menentukan elemen tengah dari data
- Membandingkan kode buku dengan elemen tengah
- Mengarahkan pencarian ke kiri atau ke kanan
- Mengulang proses hingga data ditemukan

Binary Search sangat cocok digunakan pada sistem perpustakaan karena mampu mempercepat pencarian data dalam jumlah besar.

## c. Source Code
```python
import foobar
def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Memeriksa indeks ke-{m}, kode buku: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di rak sebelah kanan")
            l = m + 1
        else:
            print("Mencari di rak sebelah kiri")
            r = m - 1
    return pos


def main():
    try:
        n = int(input("Masukkan jumlah kode buku: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan kode buku secara urut menaik:")
    for i in range(n):
        while True:
            try:
                nilai = int(input(f"Kode buku ke-{i+1}: "))
                arr.append(nilai)
                break
            except ValueError:
                print("Input harus berupa angka!")
    print(f"\nDaftar kode buku: {arr}")
    while True:
        try:
            target = int(input("Masukkan kode buku yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid!")
    pos = binary_search(arr, n, target)
    if pos != -1:
        print(f"\nBuku ditemukan pada indeks ke-{pos}")
    else:
        print("\nBuku tidak ditemukan")

if __name__ == "__main__":
    main()
```

### Penjelasan Kode
1. **Fungsi `binary_search(arr, n, target)`**
   - Digunakan untuk mencari kode buku menggunakan algoritma Binary Search.
   - Parameter:
     - `arr` -> daftar kode buku
     - `n` -> jumlah data
     - `Target` -> kode buku yang dicari

2. **Variabel `l` dan `r`**
```
l = 0
r = n - 1
```
  - `l` digunakan sebagai batas kiri array
  - `r` digunakan sebagai batas kanan array

3. **Menentukan Nilai Tengah**
```
m = l + (r - l) // 2
```
  - Digunakan untuk mencari indeks tengah array
  - Data tengah akan dibandingkan dengan target

4. Proses Pencarian
```
if arr[m] == target
```
Jika data tengah sama dengan target maka data ditemukan
```
elif arr[m] < target
```
Jika target lebih besar maka pencarian dilanjutkan ke kanan
```
else
```
Jika target lebih kecil maka pencarian dilanjutkan ke kiri

5. **Fungsi `main()`**
   - Digunakan untuk menjalankan program utama
   - User memasukkan:
     - jumlah kode buku
     - daftar kode buku
     - kode buku yang ingin dicari

6. **Output Hasil Pencarian**
  - Jika data ditemukan:
```
Buku ditemukan pada indeks ke-...
```
  - Jika data tidak ditemukan:
```
Buku tidak ditemukan
```

## d. Output Program
**Jika Data ditemukan**
```
Masukkan jumlah kode buku: 7
Masukkan kode buku secara urut menaik:
Kode buku ke-1: 101
Kode buku ke-2: 105
Kode buku ke-3: 110
Kode buku ke-4: 115
Kode buku ke-5: 120
Kode buku ke-6: 125
Kode buku ke-7: 130

Daftar kode buku: [101, 105, 110, 115, 120, 125, 130]
Masukkan kode buku yang ingin dicari: 125
Memeriksa indeks ke-3, kode buku: 115
Mencari di rak sebelah kanan
Memeriksa indeks ke-5, kode buku: 125

Buku ditemukan pada indeks ke-5
```
**Jika data tidak ditemukan**
```
Masukkan jumlah kode buku: 7
Masukkan kode buku secara urut menaik:
Kode buku ke-1: 101 
Kode buku ke-2: 105
Kode buku ke-3: 110
Kode buku ke-4: 115
Kode buku ke-5: 120
Kode buku ke-6: 125
Kode buku ke-7: 130

Daftar kode buku: [101, 105, 110, 115, 120, 125, 130]
Masukkan kode buku yang ingin dicari: 117
Memeriksa indeks ke-3, kode buku: 115
Mencari di rak sebelah kanan
Memeriksa indeks ke-5, kode buku: 125
Mencari di rak sebelah kiri
Memeriksa indeks ke-4, kode buku: 120
Mencari di rak sebelah kiri

Buku tidak ditemukan
```
## e. Link Youtube
https://youtu.be/PRLo7mu8n1c

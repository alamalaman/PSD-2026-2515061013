# Sistem Pengurutan Nilai Siswa (Selection Sort)
## a. Judul Program 
Implementasi Algoritma Selection Sort untuk Menentukan Ranking Nilai Siswa

## b. Deskripsi Singkat
Program ini merupakan implementasi algoritma Selection Sort dalam kehidupan nyata, yaitu untuk mengurutkan nilai siswa dan menentukan peringkat (ranking).
Dalam dunia pendidikan, pengurutan nilai sangat penting untuk:
- Menentukan siswa dengan nilai tertinggi
- Membuat ranking kelas
- Mempermudah analisis data akademik

Algoritma selection sort bekerja dengan mudah mencari nilai terbesar atau terkecil (opsional) dari sekumpulan data, lalu menempatkannya pada posisi yang sesuai secara bertahap hingga seluruh data terurut.
Pada program ini:
- Data diinput oleh user
- Nilai diurutkan secara descending (terbesar ke terkecil)
- Output ditampilkan dalam bentuk ranking siswa

## c. Source Code
```python
import foobar
def selection_sort(nilai):
    n = len(nilai)
    for i in range(n - 1):
        max_index = i
        for j in range(i + 1, n):
            if nilai[j] > nilai[max_index]:
                max_index = j
        
        if max_index != i:
            nilai[i], nilai[max_index] = nilai[max_index], nilai[i]


def main():
    try:
        n = int(input("Masukkan jumlah siswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    nilai = []
    print("Masukkan nilai siswa:")
    for i in range(n):
        while True:
            try:
                x = int(input(f"Nilai siswa ke-{i+1}: "))
                nilai.append(x)
                break
            except ValueError:
                print("Harus angka!")

    print("\nNilai sebelum diurutkan:", nilai)

    selection_sort(nilai)

    print("\nNilai setelah diurutkan (Ranking):")
    for i in range(n):
        print(f"Peringkat {i+1}: {nilai[i]}")


if __name__ == "__main__":
    main()
```
### Penjelasan Kode
1. **Fungsi `selection_sort(nilai)`**
- Digunakan untuk mengurutkan data nilai siswa
- Menggunakan metode Selection Sort (descending)
- Cara kerja: Mencari nilai terbesar pada setiap perulangan, dan Menukar posisi dengan elemen di depan

2. **Fungsi `main()`**
- Mengatur jalannya program
- Menerima input jumlah siswa
- Menginput nilai siswa satu per satu
- Menampilkan data sebelum dan sesudah diurutkan

3. Validasi Input
- Menggunakan `try-except`
- Mencegah error jika user memasukkan selain angka

4. Output Ranking
Data yang sudah diurutkan ditampilkan sebagai: Peringkat 1 (nilai tertinggi), kemudian peringkat berikutnya.

## d. Output Program
```
Masukkan jumlah siswa: 5
Masukkan nilai siswa:
80
90
75
85
95

Nilai sebelum diurutkan: [80, 90, 75, 85, 95]

Nilai setelah diurutkan (Ranking):
Peringkat 1: 95
Peringkat 2: 90
Peringkat 3: 85
Peringkat 4: 80
Peringkat 5: 75
```
## Penjelasan Output
1. **Input Data**
- User memasukkan jumlah siswa dan nilai masing-masing siswa.
`Masukkan jumlah siswa:`
- Nilai disimpan ke dalam list.
2. **Nilai Sebelum Diurutkan**
- Program menampilkan data awal sesuai urutan input.
``` Nilai sebelum diurutkan: [80, 90, 75, 85, 95]```
3. **Proses Sorting**
- Program menggunakan algoritma **Selection Sort**.
- Setiap iterasi mencari nilai terbesar lalu menempatkannya di posisi depan.
4. **Nilai Setelah Diurutkan**
- Data ditampilkan dalam urutan descending (terbesar ke terkecil).
``` [95, 90, 85, 80, 75]```
5. **Penentuan Ranking**
- Program menampilkan hasil dalam bentuk peringkat:
  - Peringkat 1 -> nilai tertinggi
  - Peringkat berikutnya -> nilai lebih rendah
```
Peringkat 1: 95
Peringkat 2: 90
Peringkat 3: 85
Peringkat 4: 80
Peringkat 5: 75
```

## e. Link Youtube
https://youtu.be/_4y5QyWZRv4

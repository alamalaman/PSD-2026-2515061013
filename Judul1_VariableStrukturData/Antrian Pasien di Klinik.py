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
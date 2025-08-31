import os
import sys
import time

class SimpleRootkit:
    def __init__(self):
        self.hidden_files = set()
        self.running = True

    def greet(self):
        print("Selamat datang di SimpleRootkit v2.0")
        print("Aplikasi ini hanya untuk demonstrasi fungsi dasar.\n")

    def hide_file(self, filename):
        if os.path.exists(filename):
            self.hidden_files.add(filename)
            print(f"File '{filename}' sekarang disembunyikan (simulasi).")
        else:
            print(f"File '{filename}' tidak ditemukan.")

    def list_files(self):
        print("Daftar file di direktori saat ini (file tersembunyi disembunyikan):")
        for f in os.listdir('.'):
            if f not in self.hidden_files:
                print(f" - {f}")

    def run(self):
        self.greet()
        while self.running:
            print("\nMenu:")
            print("1. List file")
            print("2. Sembunyikan file (simulasi)")
            print("3. Keluar")
            choice = input("Pilih opsi: ").strip()
            if choice == '1':
                self.list_files()
            elif choice == '2':
                filename = input("Masukkan nama file yang ingin disembunyikan: ").strip()
                self.hide_file(filename)
            elif choice == '3':
                print("Keluar dari SimpleRootkit. Terima kasih.")
                self.running = False
            else:
                print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    rootkit = SimpleRootkit()
    rootkit.run()

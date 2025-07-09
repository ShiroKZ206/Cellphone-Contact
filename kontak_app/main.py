import tkinter as tk
from utils import buat_file
from ui_tambah import tambah_kontak
from ui_kelola import kelola_kontak

def main():
    buat_file()

    root = tk.Tk()
    root.title("Manajemen Kontak")

    tk.Label(root, text="📱 Aplikasi Kontak HP", font=("Arial", 16, "bold")).pack(pady=10)

    tk.Button(root, text="Tambah Kontak", width=25, command=tambah_kontak).pack(pady=4)
    tk.Button(root, text="Kelola Kontak", width=25, command=kelola_kontak).pack(pady=4)
    tk.Button(root, text="Keluar", width=25, command=root.quit).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
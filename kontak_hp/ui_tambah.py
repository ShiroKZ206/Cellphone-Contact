import tkinter as tk
from tkinter import messagebox
from logic_tambah import simpan_kontak_baru

def tambah_kontak():
    window = tk.Toplevel()
    window.title("Tambah Kontak")

    tk.Label(window, text="Nama:").pack(pady=(10, 0))
    entry_nama = tk.Entry(window, width=30)
    entry_nama.pack(pady=5)

    tk.Label(window, text="Nomor HP:").pack()
    entry_nomor = tk.Entry(window, width=30)
    entry_nomor.pack(pady=5)

    tk.Button(
        window,
        text="Simpan",
        command=lambda: simpan_kontak_baru(entry_nama, entry_nomor, window)
    ).pack(pady=10)
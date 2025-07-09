import tkinter as tk
from tkinter import messagebox
from logic_kelola import tampilkan, cari_kontak, ubah_kontak, hapus_kontak
from utils import load_kontak

def kelola_kontak():
    window = tk.Toplevel()
    window.title("Kelola Kontak")

    kontak = load_kontak()

    top_frame = tk.Frame(window)
    top_frame.pack(pady=5)

    tk.Label(top_frame, text="Filter Huruf:").pack(side=tk.LEFT)
    filter_var = tk.StringVar(value="Semua")
    opsi = ["Semua"] + list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    tk.OptionMenu(top_frame, filter_var, *opsi,
                  command=lambda k: tampilkan(k, kontak, listbox)).pack(side=tk.LEFT)

    tk.Label(top_frame, text="Cari Nama:").pack(side=tk.LEFT, padx=10)
    entry_cari = tk.Entry(top_frame)
    entry_cari.pack(side=tk.LEFT)
    tk.Button(top_frame, text="Cari",
              command=lambda: cari_kontak(entry_cari.get(), kontak, listbox)).pack(side=tk.LEFT)

    listbox = tk.Listbox(window, width=50, height=15)
    listbox.pack(padx=10, pady=10)

    button_frame = tk.Frame(window)
    button_frame.pack(pady=5)

    tk.Button(button_frame, text="Ubah Kontak",
              command=lambda: ubah_kontak(window, kontak, listbox, filter_var, tampilkan)).pack(side=tk.LEFT, padx=10)
    tk.Button(button_frame, text="Hapus Kontak",
              command=lambda: hapus_kontak(window, kontak, listbox, filter_var, tampilkan)).pack(side=tk.LEFT, padx=10)

    tampilkan("Semua", kontak, listbox)
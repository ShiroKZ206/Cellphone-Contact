from tkinter import messagebox
from utils import load_kontak, simpan_kontak, simple_hash

def simpan_kontak_baru(entry_nama, entry_nomor, window):
    nama = entry_nama.get().strip()
    nomor = entry_nomor.get().strip()

    if not nama or not nomor:
        messagebox.showwarning("Peringatan", "Nama dan Nomor harus diisi.")
        return

    if not nomor.isdigit():
        messagebox.showerror("Input Salah", "Nomor HP harus berupa angka tanpa spasi atau huruf.")
        return

    kontak = load_kontak()
    hash_table = {}

    for n in kontak:
        h = simple_hash(n)
        if h not in hash_table:
            hash_table[h] = []
        hash_table[h].append(n)

    h_baru = simple_hash(nama)

    if h_baru in hash_table and nama in hash_table[h_baru]:
        messagebox.showerror("Gagal", "Kontak sudah ada.")
        return

    hash_table.setdefault(h_baru, []).append(nama)
    kontak[nama] = nomor
    simpan_kontak(kontak)
    messagebox.showinfo("Berhasil", f"Kontak '{nama}' ditambahkan.")
    window.destroy()
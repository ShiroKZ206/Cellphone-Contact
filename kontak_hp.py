import tkinter as tk
from tkinter import messagebox, Toplevel, Entry, Label, Button
import os
import csv

FILENAME = "kontak.csv"

def buat_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama", "Nomor"])

def load_kontak():
    kontak = {}
    if os.path.exists(FILENAME):
        with open(FILENAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                kontak[row["Nama"]] = row["Nomor"]
    return dict(sorted(kontak.items()))

def simpan_kontak(kontak):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Nomor"])
        for nama, nomor in kontak.items():
            writer.writerow([nama, nomor])

def simple_hash(key, size=1000):
    return sum(ord(char) for char in key) % size

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

def tampilkan(kriteria, kontak, listbox):
    listbox.delete(0, "end")
    for nama, nomor in kontak.items():
        if kriteria == "Semua" or nama.upper().startswith(kriteria.upper()):
            listbox.insert("end", f"{nama} : {nomor}")

def cari_kontak(keyword, kontak, listbox):
    keyword = keyword.strip().lower()
    listbox.delete(0, "end")
    for nama, nomor in kontak.items():
        if keyword in nama.lower():
            listbox.insert("end", f"{nama} : {nomor}")

def ubah_kontak(window, kontak, listbox, filter_var, refresh_fn):
    selected = listbox.get("active")
    if not selected:
        messagebox.showwarning("Pilih Kontak", "Pilih kontak yang ingin diubah.")
        return

    nama_lama, nomor_lama = selected.split(" : ")

    top = Toplevel(window)
    top.title("Ubah Kontak")

    Label(top, text="Nama Baru:").pack()
    entry_nama = Entry(top)
    entry_nama.insert(0, nama_lama)
    entry_nama.pack()

    Label(top, text="Nomor Baru:").pack()
    entry_nomor = Entry(top)
    entry_nomor.insert(0, nomor_lama)
    entry_nomor.pack()

    def simpan():
        nama_baru = entry_nama.get().strip()
        nomor_baru = entry_nomor.get().strip()
        if not nama_baru or not nomor_baru:
            messagebox.showwarning("Input Kosong", "Nama dan Nomor harus diisi.")
            return
        del kontak[nama_lama]
        kontak[nama_baru] = nomor_baru
        simpan_kontak(kontak)
        refresh_fn(filter_var.get(), kontak, listbox)
        top.destroy()

    Button(top, text="Simpan", command=simpan).pack(pady=10)

def hapus_kontak(window, kontak, listbox, filter_var, refresh_fn):
    selected = listbox.get("active")
    if not selected:
        messagebox.showwarning("Pilih Kontak", "Pilih kontak yang ingin dihapus.")
        return

    nama, _ = selected.split(" : ")
    if messagebox.askyesno("Konfirmasi", f"Yakin ingin menghapus {nama}?"):
        del kontak[nama]
        simpan_kontak(kontak)
        refresh_fn(filter_var.get(), kontak, listbox)

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

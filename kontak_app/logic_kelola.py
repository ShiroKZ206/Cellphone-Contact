from tkinter import messagebox, Toplevel, Entry, Label, Button
from utils import simpan_kontak

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

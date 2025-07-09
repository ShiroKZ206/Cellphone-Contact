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
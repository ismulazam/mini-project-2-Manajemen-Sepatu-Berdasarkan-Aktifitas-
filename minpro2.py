users = {
    "admin": {"password": "admin123", "role": "admin"},
    "user": {"password": "user123", "role": "user"}
}

list_Sepatu = [
    {"merk": "nike", "jenis": "olahraga", "aktivitas": "lari"},
    {"merk": "hoka", "jenis": "trail", "aktivitas": "hiking"}
]

#section login
def login():
    while True: 
        print("=== LOGIN ===")
        username = input("username: ")
        password = input("password: ")
        if username in users and users[username]["password"] == password:
            print(f"Login berhasil! selamat datang: {users[username]['role']}\n")
            return users[username]["role"]
        else:
            print("Username atau password salah! Coba lagi.\n")

# section create
def tambah_sepatu():
    try:
        merk = input("masukkan merk sepatu: ")
        jenis = input("masukkan jenis sepatu: ")
        aktivitas = input("masukkan aktivitas sepatu: ")
        list_Sepatu.append({"merk": merk, "jenis": jenis, "aktivitas": aktivitas})
        print("sepatu berhasil ditambahkan!\n")
    except Exception as e:
        print(f"terjadi kesalahan: {e}")

# section read
def tampilkan_sepatu():
    if not list_Sepatu:
        print("belum ada data sepatu.")
        return
    print("\ndaftar sepatu:")
    for i, sepatu in enumerate(list_Sepatu, start=1):
        print(f"{i}. merk: {sepatu['merk']}, jenis: {sepatu['jenis']}, aktivitas: {sepatu['aktivitas']}")
    print()

# section update
def update_sepatu():
    try:
        tampilkan_sepatu()
        index = int(input("masukkan nomor sepatu yang ingin diupdate: ")) - 1
        if index < 0 or index >= len(list_Sepatu):
            print("momor sepatu tidak valid.")
            return
        merk = input("Masukkan merk baru: ")
        jenis = input("Masukkan jenis baru: ")
        aktivitas = input("Masukkan aktivitas baru: ")
        list_Sepatu[index] = {"merk": merk, "jenis": jenis, "aktivitas": aktivitas}
        print("Sepatu berhasil diupdate!\n")
    except ValueError:
        print("Input harus berupa angka.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# section delete
def hapus_sepatu():
    try:
        tampilkan_sepatu()
        index = int(input("Masukkan nomor sepatu yang ingin dihapus: ")) - 1
        if index < 0 or index >= len(list_Sepatu):
            print("Nomor sepatu tidak valid.")
            return
        list_Sepatu.pop(index)
        print("sepatu berhasil dihapus!\n")
    except ValueError:
        print("nput harus berupa angka.")
    except Exception as e:
        print(f"terjadi kesalahan: {e}")

# section login role character
role = login()
if role:
    while True:
        print("=== manajemen sepatu untuk aktivitas tertentu ===")
        print("1. lihat daftar sepatu")
        print("2. tambah sepatu")
        if role == "admin":
            print("3. update sepatu")
            print("4. hapus sepatu")
        print("0. keluar")

        pilihan = input("pilih menu: ")

        if pilihan == "1":
            tampilkan_sepatu()
        elif pilihan == "2" :
            tambah_sepatu()
        elif pilihan == "3" and role == "admin":
            update_sepatu()
        elif pilihan == "4" and role == "admin":
            hapus_sepatu()
        elif pilihan == "0":
            print("baiklah terima kasih!")
            break
        else:
            print("Pilihan tidak valid.\n")
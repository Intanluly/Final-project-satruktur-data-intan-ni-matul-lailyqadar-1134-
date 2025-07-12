import csv
import os


print("=== SISTEM MANAJEMEN INVENTARIS BARANG ===")


inventory = []


DB_FILE = 'inventory_database.csv'

def init_database():
    """Inisialisasi database dari file CSV"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                inventory.append({
                    'name': row['name'],
                    'category': row['category'],
                    'quantity': int(row['quantity']),
                    'location': row['location'],
                    'description': row['description']
                })

def save_to_database():
    """Menyimpan data ke CSV"""
    with open(DB_FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'category', 'quantity', 'location', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in inventory:
            writer.writerow(item)

def add_item():
    """Fitur 1: Menambahkan barang baru ke sistem"""
    print("\n=== TAMBAH BARANG ===")
    name = input("Nama Barang: ")
    category = input("Kategori: ")
    quantity = int(input("Jumlah: "))
    location = input("Lokasi: ")
    description = input("Keterangan: ")
    
    inventory.append({
        'name': name,
        'category': category,
        'quantity': quantity,
        'location': location,
        'description': description
    })
    save_to_database()
    print(f"Barang '{name}' berhasil ditambahkan!")

def view_items():
    """Fitur 2: Menampilkan semua barang yang telah dicatat"""
    print("\n=== DAFTAR BARANG ===")
    if not inventory:
        print("Tidak ada barang yang dicatat.")
        return
    
    for idx, item in enumerate(inventory, 1):
        print(f"{idx}. Nama: {item['name']}, Kategori: {item['category']}, Jumlah: {item['quantity']}, Lokasi: {item['location']}, Keterangan: {item['description']}")

def group_by_category():
    """Fitur 3: Mengelompokkan barang berdasarkan kategori"""
    print("\n=== KELOMPOK BARANG BERDASARKAN KATEGORI ===")
    if not inventory:
        print("Tidak ada barang yang dicatat.")
        return
    
    category_dict = {}
    for item in inventory:
        category = item['category']
        if category not in category_dict:
            category_dict[category] = []
        category_dict[category].append(item)
    
    for category, items in category_dict.items():
        print(f"\nKategori: {category}")
        for item in items:
            print(f"- Nama: {item['name']}, Jumlah: {item['quantity']}, Lokasi: {item['location']}, Keterangan: {item['description']}")

def main_menu():
    """Menu utama"""
    init_database()
    
    while True:
        print("\n=== MENU UTAMA ===")
        print("1. Tambah Barang")
        print("2. Lihat Daftar Barang")
        print("3. Kelompokkan Berdasarkan Kategori")
        print("4. Keluar")
        
        choice = input("\nPilih menu: ")
        
        if choice == '1':
            add_item()
        elif choice == '2':
            view_items()
        elif choice == '3':
            group_by_category()
        elif choice == '4':
            print("Terima kasih telah menggunakan sistem kami!")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main_menu()

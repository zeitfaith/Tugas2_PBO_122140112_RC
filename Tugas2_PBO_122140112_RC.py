class Mobil:
    def __init__(self, merek, model, warna):
        self.merek = merek
        self.model = model
        self.warna = warna
        self.jarak_tempuh = 0  # Atribut tambahan untuk jarak tempuh
        self.dinyalakan = False  # Atribut tambahan untuk status mobil

    def tampilkan_info(self):
        """Menampilkan informasi tentang mobil."""
        return f"Merek: {self.merek}\nModel: {self.model}\nWarna: {self.warna}"

    def mulai(self):
        """Menyalakan mobil."""
        if not self.dinyalakan:
            self.dinyalakan = True
            print("Mobil telah dinyalakan.")
        else:
            print("Mobil sudah menyala.")

    def berhenti(self):
        """Menghentikan mobil."""
        if self.dinyalakan:
            self.dinyalakan = False
            print("Mobil telah dimatikan.")
        else:
            print("Mobil sudah dimatikan.")

    def berkendara(self, jarak):
        """Mengendarai mobil untuk jarak tertentu."""
        if self.dinyalakan:
            self.jarak_tempuh += jarak
            print(f"Mobil telah menempuh jarak {jarak} mil.")
        else:
            print("Tidak dapat berkendara. Nyalakan mobil terlebih dahulu.")

    def dapatkan_jarak_tempuh(self):
        """Mendapatkan jarak tempuh mobil."""
        return self.jarak_tempuh

    def sedang_berjalan(self):
        """Memeriksa apakah mobil sedang menyala."""
        return self.dinyalakan

# Logika utama untuk mengakses kelas dan membuat objek
if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Corolla", "Hitam")
    mobil2 = Mobil("Honda", "Civic", "Putih")

    print("Mobil 1:")
    print(mobil1.tampilkan_info())
    mobil1.mulai()
    mobil1.berkendara(50)
    print(f"Jarak Tempuh Mobil 1: {mobil1.dapatkan_jarak_tempuh()} mil")
    print(f"Apakah Mobil 1 sedang berjalan? {mobil1.sedang_berjalan()}")
    mobil1.berhenti()

    print("\nMobil 2:")
    print(mobil2.tampilkan_info())
    mobil2.mulai()
    mobil2.berkendara(30)
    print(f"Jarak Tempuh Mobil 2: {mobil2.dapatkan_jarak_tempuh()} mil")
    print(f"Apakah Mobil 2 sedang berjalan? {mobil2.sedang_berjalan()}")
    mobil2.berhenti()

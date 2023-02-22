try:
    plat_nomor = int(input("Masukkan nomor plat kendaraan: "))
    if plat_nomor >= 0 and plat_nomor <= 3000:
        print("Kendaraan tersebut adalah mobil")
    elif plat_nomor >= 3001 and plat_nomor <= 4000:
        print("Kendaraan tersebut adalah motor")
    elif plat_nomor >= 4001 and plat_nomor <= 5000:
        print("Kendaraan tersebut adalah angkutan umum")
    else:
        print("Nomor plat tidak teridentifikasi")
except ValueError:
    print("Plat Nomor Tidak Teridentifikasi, harus terdapat nomor kendaraan setelah kode daerah")
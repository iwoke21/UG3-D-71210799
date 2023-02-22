curah_hujan = float(input("Masukkan Nilai Cerah Hujan: "))

if curah_hujan == 0:
    print("Cuaca terang/berawan")
elif curah_hujan > 0 and curah_hujan <= 20:
    print("Curah hujan ringan")
elif curah_hujan > 20 and curah_hujan <= 50:
    print("Curah hujan sedang")
elif curah_hujan > 50 and curah_hujan <= 100:
    print("Curah hujan lebat")
else:
    print("Curah hujan ekstrem")
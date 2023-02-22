A = int(input("Masukkan bilangan awal: "))
B = int(input("Masukkan bilangan akhir: "))

nomor  = [i for i in range(A, B+1) if i % 6 != 0 and i % 8 != 0]

print("Deret bilangan yang tidak habis dibagi 6 atau 8:")
print(nomor)
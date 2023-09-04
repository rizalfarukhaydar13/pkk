batas = int(input("masukan batas angka: "))
jumlah_genap = 0

for angka in range (1, batas+1):
    if angka % 2 == 0:
        jumlah_genap += 1

print("jumlah angka genap dalam rentang 1 hingga", batas, "adalah: ", jumlah_genap)
# Kalkulasi dua angka
x = float(input("Angka pertama: "))
y = float(input("Angka kedua: "))

print("Hasil perhitungan:")
print("Jumlah =", x + y)
print("Selisih =", x - y)
print("Hasil kali =", x * y)
print("Hasil bagi =", x / y if y != 0 else "Tidak dapat dibagi")

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar

print(f"Luas persegi panjang: {luas} (tipe: {type(luas)})")

luas_str = str(luas)
print(f"Luas (casting ke str): '{luas_str}' (tipe: {type(luas_str)})")

usia_input = input("Masukkan usia Anda: ")

usia_int = int(usia_input)
usia_float = float(usia_input)
usia_str = str(usia_input)

print(f"Usia dalam int  : {usia_int} (tipe: {type(usia_int)})")
print(f"Usia dalam float: {usia_float} (tipe: {type(usia_float)})")
print(f"Usia dalam str  : '{usia_str}' (tipe: {type(usia_str)})")

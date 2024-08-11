# OPERASI

# index 0(-3) 1(-2) 2(-1)
data = ["Kelana", "Angan", "Pengembara"]

# mengambil data dari list
data_0 = data[0]
print(f"data pertama (index 0) = {data_0}")

data_terakhir = data[-1]
print(f"data terakhir (index -1) = {data_terakhir}")

data_kelana = data[-3]
print(f"data kelana (index -3) = {data_kelana}")

#mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"panjang data = {panjang_data}")

# manipulasi data list

# menambahkan data pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")
data.insert(1, "Dira")
print(f"data setelah ditambah = \n{data}")

# menambahkan data pada list terakhir
data.append("Dewi")
print(f"data setelah ditambah lagi = \n{data}")

# menambahkan list dengan list
data_baru = ["arsa", "arham", "gyan"]
data.extend(data_baru) 
print(f"data setelah diextend = \n{data}")

# merubah data
# misal merubah data di list ke dua
data[2] = "Penjelajah"
print(f"data setelah dirubah = \n{data}")

# meremove data
data.remove("Penjelajah")
print(f"data setelah di remove = \n{data}")

# meremove data terakhir
data.pop()
print(f"data setelah di remove terakhir = \n{data}")
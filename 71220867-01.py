keyword = input("Masukkan kata yang dicari = ")

keyword = keyword.lower()

file = 'romeojuliet.txt'
handle = open(file, 'r') 
jumlah = 0

for baris in handle:
    baris = baris.lower()
    jumlah = jumlah + baris.count(keyword)
print(f'Kata {keyword} jumlahnya ada: {jumlah}')

file = 'nilai.txt'
handle = open(file, 'r')
isi = handle.readlines()

jumlah = 0 
for i in range(len(isi)):
    print ('Nilai Tugas', i+1, ': ', isi[i])
    if i == 1 or i == 2 or i == 4:
        baru = int(isi[i])*0.5
        jumlah = jumlah + baru 
    elif i == 3 or i == 6:
        baru = int(isi[i])*0.1
        jumlah = jumlah + baru 
    elif i == 5:
        baru == int(isi[i])*0.15
        jumlah = jumlah + baru 
    elif i == 7:
        baru == int(isi[i])*0.22
        jumlah = jumlah + baru 
    elif i == 8:
        baru == int(isi[i])*0.28
        jumlah = jumlah + baru 
print ('Nilai akhir: ', round(jumlah,2))
    


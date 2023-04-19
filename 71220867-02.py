file = 'buah.txt'
handle = open(file,'r')
isi = handle.readlines()

hapus = input("Nama buah yang akan dihapus: ")

if hapus == isi[-1]:
    hapuss = "\n" + hapus 
else:
    hapuss = hapus + "\n" 
handle.close()

handle = open(file, 'r+')
isi = handle.read()

if isi.count(hapus) == 0:
    print ("Nama buah tersebut tidak ada di dalam file")
else:  
    for i in isi:
        isi = isi.replace(hapuss,"")
        handle = open(file, 'w')
        handle.write(isi)

handle.close()



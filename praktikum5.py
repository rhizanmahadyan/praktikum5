rhizan = {}
while True :
    print("")
    r = input("(T)ambah, (U)bah, (H)apus, (L)ihat, (C)ari, (K)eluar: ")
    if r.lower() == "k":
        print("Keluar Dari Sistem")
        break
   
    elif r.lower() == "l":
        print("Daftar Nilai Mahasiswa")
        print ("****************************************************************************************")
        print (" |  No |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
        print ("****************************************************************************************")
        i=0
        for x in rhizan.items():
            i+=1
            print (" |  {6:2} | {0:7s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print ("****************************************************************************************")

    elif r.lower() == "t":
        print("Tambah Data")
        nama = input ("Nama    :  ")
        nim  = int(input("NIM  :  "))
        tugas  = int(input("Nilai Tugas  :  "))
        uts  = int(input("Nilai Uts  :  "))
        uas  = int(input("Nilai Uas  :  "))
        nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
        rhizan[nama] = nim, uts, uas, tugas, nilaiakhir
 
    elif r.lower() == "u":
        print("Ubah data mahasiswa")
        nama = input("masukkan nama  :  ")
        if nama in rhizan.keys():
            nim  = int(input("NIM  :  "))
            tugas  = int(input("Nilai Tugas  :  "))
            uts  = int(input("Nilai Uts  :  "))
            uas  = int(input("Nilai Uas  :  "))
            nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
            rhizan[nama] = nim, uts, uas, tugas, nilaiakhir   
        else:
            print("Daftar Nilai Mahasiswa (0) tidak ada".format(nama))

    elif r.lower() == "h":
        print("Hapus Kontak")
        nama = input("Nama :  ")
        if nama in rhizan.keys():
                del rhizan[nama]
        else:
            print("Daftar (0) tidak ada".format(nama))

    elif r.lower() == "c":
        print("Cari daftar Nilai Mahasiswa")
        nama = input("Nama    :  ")
        if nama in rhizan.keys():
            print ("\\-------------------------DATA NILAI AKHIR MAHASISWA----------------------------------/")
            print ("****************************************************************************************")
            print ()
            print ()
            print ("========================================================================================")
            print (" |   Nama   |     NIM     |  Tugas |   UTS  |   UAS  |  NILAI |" )
            print ("=======================================================================================")
            print (" | {0:7s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(nama, nim, uts, uas, tugas, nilaiakhir))
        else:
            print("Kontak {0} tidak ada".format(nama))
    else:
        print("Pilih menu yang tersedia")

        






        



        

nilai=int(input("masukkan nilai: ")) 
daftar_hasil=[
    "selamat kamu lulus dengan predikat A+",
    "selamat kamu lulus denga predikat A",
    "selamat kamu lulus dengan B+",
    "selamat kamu lulus dengan predikat B",
    "mohon maaf kamu tidak lulus, predikat kamu C+",
    "mohon maaf kamu tidak lulus, predikat kamu C",
    "mohon maaf kamu tidak lulus, predikat kamu D+",
    "mohon maaf kamu tidak lulus, predikat kamu D",
    "mohon maaf kamu tidak lulus, predikat kamu E+",
    "mohon maaf kamu tidak lulus, predikat kamu E",
]

if nilai>=95:
    print(daftar_hasil[0])

elif nilai >=90:
    print(daftar_hasil[1])

elif nilai>=80:
    print(daftar_hasil[2])

elif nilai >= 70:
    print(daftar_hasil[3])

elif nilai>=60:
    print(daftar_hasil[4]) 

elif nilai >= 50:
    print(daftar_hasil[5])      

elif nilai >= 40 :
    print(daftar_hasil[6])

elif nilai>= 30 :
    print(daftar_hasil[7])

elif nilai >= 20 :
    print(daftar_hasil[8])

else :
    print(daftar_hasil[9])
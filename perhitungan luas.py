class persegi_panjang:
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l
    def luas(self):
        return self.panjang*self.lebar

class segitiga:
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t
    def luas(self):
        l = 1/2 * self.alas * self.tinggi
        return l

print('Perhitungan Luas Pertama')
panjang1 = int(input('Masukkan panjang persegi panjang = '))
lebar1 = int(input('Masukkan lebar persegi panjang = '))
alas1 = int(input('Masukkan alas segitiga = '))
tinggi1 = int(input('Masukkan tinggi segitiga = '))

print('Perhitungan Luas Kedua')
panjang2 = int(input('Masukkan panjang persegi panjang Kedua = '))
lebar2 = int(input('Masukkan lebar persegi panjang Kedua = '))
alas2 = int(input('Masukkan alas segitiga Kedua = '))
tinggi2 = int(input('Masukkan tinggi segitiga Kedua= '))

p1 = persegi_panjang(panjang1, lebar1)
p2 = persegi_panjang(panjang2, lebar2)
s1 = segitiga(alas1, tinggi1)
s2 = segitiga(alas2, tinggi2)

print('Luas Persegi Panjang Pertama adalah ', p1.luas())
print('Luas Segitiga Pertama adalah ', s1.luas())
print('Luas Persegi Panjang Kedua  adalah ', p2.luas())
print('Luas Segitiga Kedua adalah ', s2.luas())

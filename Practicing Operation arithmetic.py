a = 10
b = 3

#Operasi Tambah +
hasil = a + b
print(a,'+',b,'=',hasil)

#Operasi Pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

#Operasi Perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

#Operasi Pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

#Operasi Eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

#Operasi Modulus (sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)

#Operasi floor division // (pembulatan)
hasil = a // b
print(a,'//',b,'=',hasil)

#PRIORITAS OPERASI
#()
#eksponen
#perkalian
#pertambahan

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)


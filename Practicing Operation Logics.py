#Operasi Logika atau Boolean

# not, or, and, xor

#NOT
print('=====NOT=====')
a = False
c = not a
print('data a =',a)
print('------------ NOT')
print('data c =',c)


#OR
print('=====OR=====')     #jika salah satu true maka hasilnya akan true
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,'=',c)
a = True
b = False
c = a or b
print(a,'OR',b,'=',c)
a = True
b = True
c = a or b
print(a,'OR',b,'=',c)


#AND
print('=====AND=====')    #jika dua buah nilai true, makas hasilnya akan true
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,'=',c)
a = True
b = False
c = a and b
print(a,'AND',b,'=',c)
a = True
b = True
c = a and b
print(a,'AND',b,'=',c)


#XOR
print('=====XOR=====')    #jika hanya ada satu true, makas hasilnya akan true
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,'XOR',b,'=',c)
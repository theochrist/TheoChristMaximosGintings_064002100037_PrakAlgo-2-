t=("@@@@@ @   @ @@@@@ @@@@@")
u=("  @   @   @ @     @   @")
v=("  @   @@@@@ @@@@@ @   @")
w=("  @   @   @ @     @   @")
x=("  @   @   @ @@@@@ @@@@@")
print(t)
print(u)
print(v)
print(w)
print(x)

print("="*30)

#Inputan angka
a = int(input("Masukkaan angka pertama : "))
b = int(input("Masukkaan angka kedua : "))
c = int(input("Masukkaan angka ketiga : "))

#kondisi angka terbesar dan terkecil
if a > b and a > c:
  print("angka terbesar adalah : ",a)
elif b > a and b > c:
  print("angka terbesar adalah : ",b)
else:
  print("angka terbesar adalah : ",c)
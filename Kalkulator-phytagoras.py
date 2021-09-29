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

print("="*22)
print ("Kalkulator pythagoras")
print("="*22)
xinput = input("Sisi mana yang ingin anda hitung (a, b, c) : ")

if xinput == 'a':
    print("menghitung nilai sisi a")
    b = int(input("masukkan nilai b : "))
    c = int(input("masukkan nilai c : "))
    a = ((c**2)-(b**2))**.5

    if c < b :
        print("error : nilai c lebih kecil dari a & b")
    elif c > b :
        print("nilai c : ", a)
    else :
        print(" error ")

elif xinput == 'b' :
    print("menghitung nilai sisi b")
    a = int(input("masukkan nilai a : "))
    c = int(input("masukkan nilai c : "))
    b = ((c**2)-(a**2))**.5

    if c < a :
        print("error : nilai c lebih kecil dari a & b")
    elif c > a :
        print("nilai b : ", b)
    else :
        print(" error ")

elif xinput == 'c' :
    print("menghitung nilai sisi c")
    a = int(input("masukkan nilai a : "))
    b = int(input("masukkan nilai b : "))
    c = ((a**2)+(b**2))**.5

    print("nilai c : ", c)
else :
    print("Inputan salah")
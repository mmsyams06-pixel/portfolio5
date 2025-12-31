def kalkulator (operasi, a, b):
    if operasi == "*":
        return a*b
    elif operasi == "+":
        return a+b
    elif operasi == "-":
        return a-b
    elif operasi == "/":
        if b == 0:
            return "Error: Pembagian 0"
        else:
            return a/b
    else: 
        return "Operasi Tidak Valid"
    
for i in range(3):
    print (f"\n Iterasi ke {i+1}")
    
    operasi = ""
    while operasi not in ["*","-","+","/"]:
        operasi = input("Masukkan operasi (*,+,-,/): ")
    
    a  = None
    while a is None or a <= 0:
        try:
            a = float(input("Masukkan angka pertama (Positif): "))
            if a <= 0:
                print("Angka harus positif. Coba lagi!: ")
        except ValueError:
            print("Input harus angka. Coba lagi!: ")
    
    b = None
    while b is None or b <= 0:
        try:
            b = float(input("Masukkan angka kedua (Positif): "))
            if b <= 0:
                print("Angka harus positif. Coba lagi!: ")
        except ValueError:
            print("Input harus angka. Coba lagi!: ")

    Hasil = kalkulator(operasi, a, b)
    print (f"Hasilnya adalah {Hasil}")

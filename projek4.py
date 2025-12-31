def konversi_suhu (suhu, skala1, skala2):
    if skala1 == "C" and skala2 == "F":
        return (suhu*9/5) + 32
    elif skala1 == "C" and skala2 == "R":
        return suhu*4/5
    elif skala1 == "C" and skala2 == "K":
        return suhu + 273
    elif skala1 == "F" and skala2 == "C":
        return (suhu-32)*5/9
    elif skala1 == "F" and skala2 == "R":
        return (suhu-32)*4/9
    elif skala1 == "F" and skala2 == "K":
        return 5/9*(suhu-32)+273
    elif skala1 == "K" and skala2 == "C":
        return suhu - 273
    elif skala1 == "K" and skala2 == "F":
        return 9/5*(suhu-273)+32
    elif skala1 == "K" and skala2 == "R":
        return 4/5*(suhu-273)
    elif skala1 == "R" and skala2 == "C":
        return 5/4*suhu
    elif skala1 == "R" and skala2 == "F":
        return 9/4*suhu + 32
    elif skala1 == "R" and skala2 == "K":
        return 5/4*suhu + 273
    else:
        return None
    
for i in range(3):
    print(f"\nIterasi ke {i+1}")

    skala1 = ""
    while skala1 not in ["C","F", "R", "K"]:
        skala1 = input("Masukkan skala awal (C/F/R/K): ").upper()
   
    suhu = None
    while suhu is None:
        try:
            suhu = float(input("Masukkan suhu!: "))
        except ValueError:
            print("Suhu harus berupa angka. Coba Lagi!: ")

    skala2 = ""
    while skala2 not in ["C","F", "R", "K"]:
        skala2 = input("Masukkan skala tujuan (C/F/R/K): ").upper()

    konversi = konversi_suhu(suhu, skala1, skala2)

    print(f"{suhu}  {skala1} = {konversi}  {skala2}")
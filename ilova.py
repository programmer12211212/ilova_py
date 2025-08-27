import vazifa

def menu():
    print("1 - Vazifa qo‘shish")
    print("2 - Ro‘yxatni ko‘rish")
    print("3 - Vazifani o‘chirish")
    print("0 - Chiqish")

vazifa.yuklash()

while True:
    menu()
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        yangi = input("yangi vazifa kiriting: ")
        vazifa.qoshish(yangi)
    elif tanlov == "2":
        vazifa.korish()
    elif tanlov == "3":
        vazifa.korish()
        raqam = input("o‘chirmoqchi bo‘lgan vazifa raqamini kiriting: ")
        vazifa.ochirish(raqam)
    elif tanlov == "0":
        vazifa.saqlash()
        print("dastur tugadi")
        break

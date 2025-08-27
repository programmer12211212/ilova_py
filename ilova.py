topshiriq = []

def menu():
    print("1 - Vazifa qo‘shish")
    print("2 - Ro‘yxatni ko‘rish")
    print("3 - Vazifani o‘chirish")
    print("0 - Chiqish")

while True:
    menu()
    tanlov = input("Tanlang: ")

    if tanlov == "1":
        vazifa = input("yangi vazifa kiriting: ")
        topshiriq.append(vazifa)
        print("vazifa qo‘shildi...")
    elif tanlov == "2":
        if not topshiriq:
            print("xali vazifalar yoq")
        else:
            print("\n--- Vazifalar ro‘yxati ---")
            for i, t in enumerate(topshiriq, start=1):
                print(f"{i}. {t}")
    elif tanlov == "3":
        if not topshiriq:
            print("xali vazifalar yoq, o‘chirish mumkin emas")
        else:
            print("Vazifalar ro‘yxati:")
            for i, t in enumerate(topshiriq, start=1):
                print(f"{i}. {t}")
            try:
                raqam = int(input("o‘chirmoqchi bo‘lgan vazifa raqamini kiriting: "))
                if 1 <= raqam <= len(topshiriq):
                    ochirilgan = topshiriq.pop(raqam - 1)
                    print(f"vazifa o‘chirildi: {ochirilgan}")
                else:
                    print("bunday raqamli vazifa yo‘q")
            except ValueError:
                print("iltimos, faqat raqam kiriting")
    elif tanlov == "0":
        print("dastur tugadi")
        break

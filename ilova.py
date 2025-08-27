
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
            for i, topshiriq in enumerate(topshiriq, start=1):
                print(f"{i}. {topshiriq}")
    elif tanlov == "0":
        print("dastur tugadi")
        break

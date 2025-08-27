def menyu():
    print("\n--- Vazifa Ilova ---")
    print("1 - Vazifa qo‘shish")
    print("2 - Ro‘yxatni ko‘rish")
    print("3 - Vazifani o‘chirish")
    print("0 - Chiqish")

def main():
    while True:
        menyu()
        tanlov = input("Tanlovni kiriting: ")
        if tanlov == "0":
            print("Dasturdan chiqildi.")
            break
        else:
            print("Bu funksiya hali ishlamaydi.")

if __name__ == "__main__":
    main()

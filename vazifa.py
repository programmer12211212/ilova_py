topshiriq = []

def yuklash():
    try:
        with open("malumotlar.txt", "r", encoding="utf-8") as f:
            for qator in f:
                topshiriq.append(qator.strip())
    except FileNotFoundError:
        pass

def saqlash():
    with open("malumotlar.txt", "w", encoding="utf-8") as f:
        for t in topshiriq:
            f.write(t + "\n")

def qoshish(vazifa):
    if vazifa.strip() == "":
        print("bo‘sh vazifa qo‘shib bo‘lmaydi")
    else:
        topshiriq.append(vazifa.strip())
        print("vazifa qo‘shildi...")

def korish():
    if not topshiriq:
        print("xali vazifalar yoq")
    else:
        print(":vazifalar ro‘yxat")
        for i, t in enumerate(topshiriq, start=1):
            print(f"{i}. {t}")

def ochirish(raqam):
    if not topshiriq:
        print("xali vazifalar yoq, o‘chirish mumkin emas")
    elif not raqam.isdigit():
        print("iltimos, faqat raqam kiriting")
    else:
        raqam = int(raqam)
        if 1 <= raqam <= len(topshiriq):
            ochirilgan = topshiriq.pop(raqam - 1)
            print(f"vazifa o‘chirildi: {ochirilgan}")
        else:
            print("bunday raqamli vazifa yo‘q")

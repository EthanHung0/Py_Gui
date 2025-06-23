with open("13.txt",mode="w",encoding="utf-8") as a:
    a.write("aduangseng")

with open("13.txt",mode="r",encoding="utf-8") as a:
    adu = a.read()
    print(adu)

with open("13.txt",mode="a",encoding="utf-8") as a:
    a.write("\nbaohoanglonlon")

with open("13.txt",mode="r",encoding="utf-8") as a:
    adulonlon = a.read()
    print(adulonlon)

shopping = ["برنج", "تخم مرغ", "شیر", "نان"]

shopping.append("ماست")

shopping.remove("شیر")

print(shopping)

print(len(shopping))

print("برنج" in shopping)

shopping.sort()
print(shopping)

x = input()
if x in shopping:
    shopping.remove(x)
    print(shopping)
else:
    print("این کالا در لیست وجود ندارد")

print("Chương trình tính tiền điện tiêu thụ")

amount_of_elec_consumed = int(input("Nhập số điện tiêu thụ: "))

if amount_of_elec_consumed <= 50:
    total = amount_of_elec_consumed * 2000
elif 51 <= amount_of_elec_consumed <= 100:
    total = amount_of_elec_consumed * 2500
else:
    total = amount_of_elec_consumed * 3000

print(total)
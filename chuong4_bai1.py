print("Chương trình xếp loại học sinh")

test_score = input("Nhập điểm trung bình (0-10): ")

if test_score.isdigit() == True:

    test_score = int(test_score)  
    if 9 <= int(test_score) <= 10:
        print("Xuất sắc")
    elif 8 <= int(test_score) <= 8.9:
        print("Giỏi")
    elif 6.5 <= int(test_score) <= 7.9:
        print("Khá")
    elif 5 <= int(test_score) <= 6.4:
        print("Trung bình")
    elif int(test_score) < 5:
            print("Yếu")
    else:
         print("Điểm không hợp lệ")
else:
    print("Điểm không hợp lệ")
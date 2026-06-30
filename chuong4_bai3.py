level_of_study = input("Nhập cấp học: (nhập số): ")

match level_of_study:
    case "1":
        math = float(input("Nhập điểm toán: "))
        literature = float(input("Nhập điểm văn: "))
        english = float(input("Nhập điểm anh: "))
        average = (math + literature + english) / 3
        print(f"Điểm trung bình Cấp {level_of_study} = {average}")
    case "2":
        math = float(input("Nhập điểm toán: "))
        literature = float(input("Nhập điểm văn: "))
        english = float(input("Nhập điểm anh: "))
        average = (math * 2 + literature * 2 + english) / 5
        print(f"Điểm trung bình Cấp {level_of_study} = {average}")
    case "3":
        math = float(input("Nhập điểm toán: "))
        literature = float(input("Nhập điểm văn: "))
        english = float(input("Nhập điểm anh: "))
        average = (math + literature + english * 2) / 4
        print(f"Điểm trung bình Cấp {level_of_study} = {average}")
    case _:
        print("Cấp học không hợp lệ")


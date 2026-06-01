list_vehicle = []
next_id = 1

while True:
    choice = input("""QUẢN LÝ BAI XE - SMART PARKING

1. Thêm xe mới vào bãi
2. Hien thị danh sách xe trong bãi
3. Tìm kiêm xe theo mã (id)
4. Xóa xe khỏi bãi (khi xe ra)
5. Thoat chương trinh
===========================================                   
Nhập lựa chọn (1-5):                   """)
    match choice:
        case '1':
            while True:
                vehicle_type = input("Nhập loại xe: ").strip()
                if vehicle_type != "":
                    break
                print("Lỗi: Loại xe không được để trống! Vui lòng nhập lại.")

            while True:
                vehicle_owner = input("Nhập tên chủ xe: ").strip()
                if vehicle_owner != "":
                    break
                print("Lỗi: Chủ xe không được để trống! Vui lòng nhập lại.")
            new_vehicle = {
                "id": next_id,
                "type": vehicle_type,
                "owner": vehicle_owner,
            }
            list_vehicle.append(new_vehicle)
            print(f"Thêm xe mới thành công với ID: {next_id}")
            next_id += 1

        case '2':
            print("====== DANH SÁCH XE ======")
            if not list_vehicle:
                print("Bãi xe hiện đang trống!")
            else:
                for i in list_vehicle:
                    print(f"{i['id']}      |{i['type']}   |{i['owner']}")
        case "3":
            search_id = int(input("Nhập ID cần tìm: ").strip())
            found_vehicle = None
            for vehicle in list_vehicle:
                if vehicle["id"] == search_id:
                    print("Thông tin xe:",vehicle)
                    break

            if found_vehicle is None:
                print(f"Không tìm thấy xe có ID [{search_id}]!")

        case '4':
            delete_id = int(input("Nhập ID xe cần xóa: "))
            index = -1
            for idx, vehicle in enumerate(list_vehicle):
                if vehicle["id"] == delete_id:
                    index = idx
                    break
                    
            if index != -1:
                list_vehicle.pop(index)
                print(f"Đã xóa xe ID [{delete_id}] thành công!")
            else:
                print("Không tìm thấy xe để xóa!") 
                
        case '5':
            print("Đã thoát chương trình. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")
            break
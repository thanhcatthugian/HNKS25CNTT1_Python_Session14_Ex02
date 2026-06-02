total_point = 100
def add_reward_points(bonus):
    global total_point 
    total_point = total_point+bonus
    print(f"Đã cộng thêm {bonus} điểm")

add_reward_points(50)
print(f"Tổng điểm hiện tại của khách hàng: {total_point}")

'''
    Trả lời câu hỏi
    Biến total_points được khai báo ở dòng 2 là biến toàn cục (Global) hay cục bộ (Local)? Tại sao?
    toàn cục, do chưa khai báo total
    Hãy giải thích thông báo lỗi: UnboundLocalError: local variable 'total_points' referenced before assignment. Tại sao Python lại coi total_points bên trong hàm là biến cục bộ (local variable) dù bên ngoài đã khai báo rồi?
    vì cần khai báo global cho biến ở trong hàm thay vì ở ngoài
    Nếu chúng ta chỉ muốn đọc (print) biến total_points bên trong hàm thay vì thay đổi (gán) nó thì chương trình có bị lỗi không?
    vẫn sẽ có lỗi, vì print đang được yêu cầu in ra một biến chưa được khai báo
    Cách sửa 1: Từ khóa (keyword) nào trong Python giúp chúng ta khai báo bên trong hàm rằng: "Hãy sử dụng và thay đổi biến toàn cục ở bên ngoài, đừng tạo biến cục bộ mới"? Viết lại dòng lệnh đó.
    global total_point
    Cách sửa 2 (Clean code hơn - Ưu tiên): Thay vì can thiệp trực tiếp vào biến toàn cục, một hàm tốt (pure function) nên nhận tham số đầu vào (tổng điểm cũ, điểm mới) và dùng lệnh gì để trả về tổng điểm đã cộng?
    sử dụng return total_point 
'''
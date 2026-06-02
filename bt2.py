total_point = 100
def add_reward_points(bonus):
    global total_point 
    total_point = total_point+bonus
    print(f"Đã cộng thêm {bonus} điểm")

add_reward_points(50)
print(f"Tổng điểm hiện tại của khách hàng: {total_point}")

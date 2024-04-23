import math

"""Core Requirements"""
def compute_volume(can_height, can_radius):
    volume = math.pi * (can_radius ** 2) * can_height
    return volume

def compute_surface_area(can_height, can_radius):
    surface_area = 2 * math.pi * can_radius * (can_radius + can_height)
    return surface_area

# def main():
#     """this isn't an easy way to do the task"""
#     can_height_can_1 = 10.16
#     can_radius_can_1 = 6.83
#     volume_can_1 = compute_volume(can_height_can_1, can_radius_can_1)
#     surface_area_can_1 = compute_surface_area(can_height_can_1, can_radius_can_1)
#     storage_efficiency_can_1 = volume_can_1 / surface_area_can_1
#     print(f"#1 Picnic {storage_efficiency_can_1}")

"""Core Requirements + a modification"""
def compute_storage_efficiency(can_height, can_radius):
    """Added to ease the task"""
    volume = compute_volume(can_height, can_radius)
    surface_area = compute_surface_area(can_height, can_radius)
    storage_efficiency = volume / surface_area
    return storage_efficiency

# def main():
#     can_1 = compute_storage_efficiency(10.16, 6.83)
#     can_2 = compute_storage_efficiency(11.91, 7.78)
#     can_3 = compute_storage_efficiency(11.59, 8.73)
#     can_4 = compute_storage_efficiency(11.91, 10.32)
#     can_5 = compute_storage_efficiency(17.78, 10.79)
#     can_6 = compute_storage_efficiency(14.29, 13.02)
#     can_7 = compute_storage_efficiency(8.89, 5.40)
#     can_8 = compute_storage_efficiency(7.62, 6.83)
#     can_9 = compute_storage_efficiency(17.78, 15.72)
#     can_10 = compute_storage_efficiency(12.38, 6.83)
#     can_11 = compute_storage_efficiency(11.27, 7.62)
#     can_12 = compute_storage_efficiency(11.11, 8.10)
#     print(f"#1 Picnic {can_1:.2f}")
#     print(f"#1 Tall {can_2:.2f}")
#     print(f"#2 {can_3:.2f}")
#     print(f"#2.5 {can_4:.2f}")
#     print(f"#3 Cylinder {can_5:.2f}")
#     print(f"#5 {can_6:.2f}")
#     print(f"#6Z {can_7:.2f}")
#     print(f"#8Z short {can_8:.2f}")
#     print(f"#10 {can_9:.2f}")
#     print(f"#211 {can_10:.2f}")
#     print(f"#300 {can_11:.2f}")
#     print(f"#303 {can_12:.2f}")

"""Stretch Challenges"""
can_list = ["#1 Picnic,10.16,6.83,0.28", "#1 Tall,11.91,7.78,0.43", "#2,11.59,8.73,0.45", "#2.5,11.91,10.32,0.61", "#3 Cylinder,17.78,10.79,0.86", "#5,14.29,13.02,0.83", "#6Z,8.89,5.40,0.22", "#8Z short,7.62,6.83,0.26", "#10,17.78,15.72,1.53", "#211,12.38,6.83,0.34", "#300,11.27,7.62,0.38", "#303,11.11,8.10,0.42"] # list challenge

def compute_cost_efficiency(can_height, can_radius, can_cost): # compute cost challenge
    volume = compute_volume(can_height, can_radius)
    cost_efficiency = volume / can_cost
    return cost_efficiency

def main():
    print("\nCan name, Storage efficiency")
    best_storage_efficiency = 0
    for can in can_list: # list challenge
        can_elements = can.split(",")
        can_name = can_elements[0]
        can_height = float(can_elements[1])
        can_radius = float(can_elements[2])
        can_cost = float(can_elements[3])
        storage_efficiency = compute_storage_efficiency(can_height, can_radius)
        cost_efficiency = compute_cost_efficiency(can_height, can_radius, can_cost)
        print(f"{can_name} {storage_efficiency:.2f}")
        if storage_efficiency > best_storage_efficiency: # if challenge
            best_storage_efficiency = storage_efficiency
            best_can_name = can_name
    print(f"The can {best_can_name} has the best storage eficency with {best_storage_efficiency:.2f} ratio.\n")
    print("\nCan name, Cost efficiency")
    best_cost_efficiency = 0  # compute cost challenge
    for can in can_list: # list challenge
        can_elements = can.split(",")
        can_name = can_elements[0]
        can_height = float(can_elements[1])
        can_radius = float(can_elements[2])
        can_cost = float(can_elements[3])
        storage_efficiency = compute_storage_efficiency(can_height, can_radius)
        cost_efficiency = compute_cost_efficiency(can_height, can_radius, can_cost)
        print(f"{can_name} {cost_efficiency:.2f}")
        if cost_efficiency > best_cost_efficiency: # if challenge
            best_cost_efficiency = cost_efficiency
            best_can_name = can_name
    print(f"The can {best_can_name} has the best cost eficency with {best_cost_efficiency:.2f} ratio.\n")

"""showtime caller"""
main()
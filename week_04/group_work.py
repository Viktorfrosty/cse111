import math

can_list = ["#1 Picnic, 6.83, 10.16, 0.28", "#1 Tall, 7.78, 11.91, 0.43", "#2, 8.73, 11.59, 0.45", "#2.5, 10.32, 11.91, 0.61", "#3 Cylinder, 10.79, 17.78, 0.86", "#5, 13.02, 14.29, 0.83", "#6Z, 5.4,8.89, 0.22", "#8Z short, 6.83, 7.62, 0.26", "#10, 15.72, 17.78, 1.53", "#211, 6.83, 12.38, 0.34", "#300, 7.62, 11.27, 0.38", "#303, 8.1, 11.11, 0.42"]

def compute_cost_efficiency(can_height, can_radius, can_cost):
    volume = compute_volume(can_height, can_radius)
    cost_efficiency = volume / can_cost
    return cost_efficiency

def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    surf_area = 2 * math.pi * radius * (radius + height)
    return surf_area

def compute_storage_efficiency(can_height, can_radius):
    volume = compute_volume(can_height, can_radius)
    surface_area = compute_surface_area(can_height, can_radius)
    storage_efficiency = volume / surface_area
    return storage_efficiency

def main():
    best_cost_efficiency = 0
    for can in can_list:
        can_elements = can.split(",")
        can_name = can_elements[0]
        can_height = float(can_elements[1])
        can_radius = float(can_elements[2])
        can_cost = float(can_elements[3])
        cost_efficiency = compute_cost_efficiency(can_height, can_radius, can_cost)
        print(f"{can_name} {cost_efficiency:.2f}")
        if cost_efficiency > best_cost_efficiency:
            best_cost_efficiency = cost_efficiency
            best_can_name = can_name
    print(f"The can {best_can_name} has the best storage efficiency with {best_cost_efficiency:2f} ratio.")

main()
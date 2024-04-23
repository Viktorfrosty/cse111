def main():
    province_list = []
    province_list = read_list("week_09\provinces.txt", province_list)
    print(province_list)
    print()
    province_list = altern_list(province_list)
    print(province_list)
    province = "Alberta"
    province_counted = province_count(province, province_list)
    print(f"{province} occurs {province_counted} times in the list")

def read_list(filename, province_list):
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            province_list.append(clean_line)
    return province_list

def altern_list(province_list):
    province_list.pop(0)
    province_list.pop()
    for i in range(len(province_list)):
            if province_list[i] == "AB":
                province_list[i] = "Alberta"
    return province_list

def province_count(province, province_list):
    count = province_list.count(province)
    return count

if __name__ == "__main__":
    main()
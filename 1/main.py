def total_salary(path: str):

    total = 0
    str_count = 0

    with open(path, encoding="utf-8") as salary:
        for string in salary:
            res = string.strip().split(",")
            total += int(res[1])
            str_count += 1

    ret = (total, int(total/str_count))
    return ret

# total, average = total_salary("1/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
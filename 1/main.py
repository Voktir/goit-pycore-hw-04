def total_salary(path: str):

    total = 0
    str_count = 0

    try:

        with open(path, encoding="utf-8") as salary:
            for string in salary:
                try:
                    res = string.strip().split(",")
                    total += int(res[1])
                    str_count += 1
                except:
                    continue
        
        ret = (total, int(total/str_count))
        return ret
    
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

# total, average = total_salary("1/salary_file.txt")
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
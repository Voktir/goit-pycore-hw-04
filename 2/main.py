def get_cats_info(path):

    lst = []

    with open(path, encoding="utf-8", errors='replace') as cats:
        for string in cats:
            res = string.strip().split(",")
            try:
                if len(res)<=3:
                    cats_dict = {"id": res[0], "name": res[1], "age": res[2]}
                else:
                    continue
            except:
                continue
            lst.append(cats_dict)

    return lst

# cats_info = get_cats_info("2/cats_file.txt")
# print(cats_info)
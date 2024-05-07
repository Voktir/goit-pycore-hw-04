# def generator_numbers(text: str):

#     # pattern = r'\d{*}\.\d{*}'
    
#     # i = re.findall(pattern, text)   
    
#     i = [ 1.00, 2.5, 3.3, 0.1]

#     print(i)

#     for n in i:
#         yield n #float(n)

# import sys
# from pathlib import Path
# from scan import scan_dir

# def main():
#     if len(sys.argv) > 1:
#         root_dir = Path(sys.argv[1])
#         if (not root_dir.exists() or not root_dir.is_dir()):
#             print("Not directory or does not exitsts")
#             return
#         scan_dir(root_dir)

# if __name__ == "__main__":
#     main()


# from colorama import Fore

# print_colors = {
#     "dir": Fore.BLUE,
#     "file": Fore.GREEN,
#     "": Fore.WHITE,
# }

# def print_out(type: str, line: str):
#     print(f"{print_colors.get(type)}{line}{Fore.RESET}")


# from pathlib import Path
# from printout import print_out

# def scan_dir(directory: Path, tabs: str=""):
#     print_out("dir", f"{tabs}{directory.name}\\")
#     tabs += "    "
#     for path in directory.iterdir():
#         if (path.is_dir()):
#             scan_dir(path, tabs)
#         elif (path.is_file()):
#             print_out("file", f"{tabs}{path.name}")
#         else:
#             print_out("",f"{tabs}Unknown entity")

# x = 12.34567
# print(type(f"{x:.2f}"))

        
from pathlib import Path
from colorama import Fore, Back, Style


def p_elmnts(path):
    for el in path.iterdir():
        s = f"{el}"
        if s.find("\\") == -1 :
            spliter = "/"
        if s.find("/") == -1 :
            spliter = "\\"
        s = " " * ((len(f"{el}".split(spliter)) - 1)*3)
        if el.is_dir():
            print(Fore.CYAN + f"{s}{el.relative_to(Path(el).parent)}\\" + Style.RESET_ALL)
            p_elmnts(el)
        else:            
            print(Fore.GREEN + f"{s}{el.relative_to(Path(el).parent)}" + Style.RESET_ALL)
            

def main():
    path_input = ""
    while True:
        print("")
        print(Fore.BLUE + "Вітаю, цей застосунок приймає шлях до директорії в якості аргументу командного рядка\n і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів" + Style.RESET_ALL)            
        print("")
        path_choise = input(Fore.MAGENTA + "      Введіть 1 для демо режиму, чи 2 для вводу шляху вручну: " + Style.RESET_ALL)
        match path_choise:
            case "1":                
                path_input = "3"
                print(Fore.CYAN + f"{path_input}\\" + Style.RESET_ALL)
                p_elmnts(Path(path_input))
            case "2":
                path_input = input(Fore.YELLOW + "Уважно введіть шлях вручну: " + Style.RESET_ALL)
                print(Fore.CYAN + f"{Path(path_input)}\\" + Style.RESET_ALL)
                try:
                    p_elmnts(Path(path_input))
                except:
                    print (Fore.RED + "Помилка шляху. Уважно вводьте шлях!" + Style.RESET_ALL)
            case _:
                print (Fore.RED + "Зробіть правильний вибір: введіть 1 чи 2" + Style.RESET_ALL)


if __name__ == "__main__":
    main()
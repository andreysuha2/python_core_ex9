from dictionary.main import dictionary, save_dictionary
from input_handler import get_comand
from comands import HANDLERS

def close():
    save_dictionary()
    print("Thank you! Your dictionary is saved")

def main():
    while True:
        try:
            enter_string = input(">>> ")
            input_handler = get_comand(enter_string)
            is_close = next(input_handler)
            if is_close:
                close()
                break
            comand_exist, comand, args = next(input_handler)
            if comand_exist:
                result = HANDLERS[comand](args)
                print(f"{result}\n")
            else:
                print(f'Comand "{comand}" not found')
        except KeyboardInterrupt:
            close()
            break

if __name__ == "__main__":
    main()
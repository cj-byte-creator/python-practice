from logic import Calculator

first_run = True
calc = Calculator()

def try_parse_float(value):
    try:
        return float(value)
    except ValueError:
        return None
        
def operation_valid(operation):
    match operation:
        case "a"|"+"|"s"|"-"|"m"|"*"|"d"|"/":
            return True
        case _:
            return False
        
def do_operation(operation,number):
    match operation:
        case "a" | "+":
            calc.add(number)
            print_calculation()
        case "s" | "-":
            calc.subtract(number)
            print_calculation()
        case "m" | "*":
            calc.multiply(number)
            print_calculation()
        case "d" | "/":
            try:
                calc.divide(number)
                print_calculation()
            except ZeroDivisionError:
                print("Cannot divide by Zero!")

def print_calculation():
    print(calc.last_total, operation_map.get(operation), float(num), "=", calc.total)

def quit(num="",operation=""):
    if num == "q" or operation == "q":
        return True
    else:
        return False

print("----- Calculator -----")
operation_map = {
    'a': '+',
    '+': '+',
    's': '-',
    '-': '-',
    'm': 'x',
    '*': 'x',
    'd': '/',
    '/': '/'
}
if __name__ == "__main__":
    while True:
        if calc.total is None:
            num = input("(q to quit) Input number : ")
            if quit(num):
                break
            parsed_num = try_parse_float(num)
            while parsed_num is None:
                num = input("Enter a valid number! : ")
                if quit(num):
                    break
                parsed_num = try_parse_float(num)
            calc.add(parsed_num)
            continue

        operation = input("Choose operation: \n 'a' or '+' - add \n 's' or '-' - subtract \n 'm' or '*' - multiply \n 'd' or '/' - divide \n 'q' - quit \n").lower()
        if quit(operation):
            break

        while not operation_valid(operation):
                operation = input("Enter a valid operation! : ")

        num = input("(q to quit) Input number : ")
        if quit(num):
            break
        parsed_num = try_parse_float(num)
        while parsed_num is None:
            num = input("Enter a valid number! : ")
            if quit(num):
                break
            parsed_num = try_parse_float(num)
            
        do_operation(operation,parsed_num)

print("----- Thank you! -----")





        


        

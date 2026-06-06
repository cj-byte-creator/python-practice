from logic import Calculator

first_run = True
calc = Calculator()

def num_valid(number):
        try:
            number = float(number)
            return True
        except ValueError:
            return False
        
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
            
            if num_valid(num):
                calc.add(float(num))
            else:
                print("Enter a valid number.")
            continue

        operation = input(f"Choose operation: \n 'a' or '+' - add \n 's' or '-' - subtract \n 'm' or '*' - multiply \n 'd' or '/' - divide \n 'q' - quit \n").lower()
        if quit(operation):
            break

        while not operation_valid(operation):
                operation = input("Enter a valid operation! : ")

        num = input("(q to quit) Input number : ")
        if quit(num):
            break
        while not num_valid(num):
            num = input("Enter a valid number! : ")
            
        do_operation(operation,float(num))

print("----- Thank you! -----")





        


        

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
        case "s" | "-":
            calc.subtract(number)
        case "m" | "*":
            calc.multiply(number)
        case "d" | "/":
            calc.divide(number)
    
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
        if first_run == False:#second - continuous runs
            num = input(f"(q to quit) Input number : ")
            if quit(num):
                break
            
            if num_valid(num):
                num = float(num)
            operation = input(f"Choose operation: \n 'a' or '+' - add \n 's' or '-' - subtract \n 'm' or '*' - multiply \n 'd' or '/' - divide \n 'q' - quit \n").lower()
            if quit(operation):
                break

            while not operation_valid(operation):
                    operation = input("Enter a valid operation! : ")
            do_operation(operation,num)
            print(calc.last_total, operation_map.get(operation), num, "=", calc.total)
            
        else:#first run
            num = input(f"(q to quit) Input number : ")
            if quit(num):
                break

            if num_valid(num):
                first_run = False
                num = float(num)
                calc.add(num)

                operation = input(f"Choose operation: \n 'a' or '+' - add \n 's' or '-' - subtract \n 'm' or '*' - multiply \n 'd' or '/' - divide \n 'q' - quit \n").lower()
                if quit(operation):
                    break

                while not operation_valid(operation):
                    operation = input("Enter a valid operation! : ")

                num = input("Input a number : ")
                while not num_valid(num):
                    num = input("Enter a valid number! : ")

                num = float(num)
                do_operation(operation,num)
                print(calc.last_total, operation_map.get(operation), num, "=", calc.total)
            else:
                print ("Enter a valid number.")

print("----- Thank you! -----")





        


        

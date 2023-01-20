
# define all messages
msg_ = ["Enter an equation", # msg_0
        "Do you even know what numbers are? Stay focused!", # msg_1
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?", # msg_2
        "Yeah... division by zero. Smart move...", # msg_3
        "Do you want to store the result? (y / n):", # msg_4
        "Do you want to continue calculations? (y / n):", # msg_5
        " ... lazy", # msg_6
        " ... very lazy", # msg_7
        " ... very, very lazy", # msg_8
        "You are", # msg_9
        "Are you sure? It is only one digit! (y / n)", # msg_10
        "Don't be silly! It's just one number! Add to the memory? (y / n)", # msg_11
        "Last chance! Do you really want to embarrass yourself? (y / n)" # msg_12
        ]

# function to determine if a number is a one-digit integer
def is_one_digit(v): 
    if v > -10 and v < 10 and v.is_integer():
        return True
    else:
        return False

# function to check if the calculation is easy    
def check(v1, v2, v3):
    msg = ""
    
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_[6]
        
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_[7]
        
    if (v1 == 0 or v2 == 0) and (v3 == "+" or v3 == "-" or v3 == "*"):
        msg = msg + msg_[8]

    if msg != "":
        msg = msg_[9] + msg
        
    print(msg)


# Calculate the result

memory = 0

while True:
    print(msg_[0]) # "Enter an equation"
    (x, oper, y) = input().split()
    
    if x == "M":
        x = memory
    
    if y == "M":
       y = memory
    
    # check if x and y are numbers
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue

    # check if the operator is correct
    if oper not in "+" "-" "*" "/":
        print(msg_[2])
        continue
    
    check(x, y, oper)
    
    # calculation if not division by zero
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/" and y != 0:
        result = x / y
    else:
        print(msg_[3])
        continue

    print(result)

    while True:
        print(msg_[4])
        answer = input()
        if answer == "y":
            
            # save the memory
            if is_one_digit(result):
                
                msg_index = 10
                
                while True:
                    print(msg_[msg_index])  
                    answer = input()
                    if answer == "y":
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer == "n":
                        break
                    else:
                        continue
                    
            else:
                memory = result
                
            break
        elif answer == "n":
            break
        else:
            continue
    
    while True:
        print(msg_[5])
        answer = input()
        if answer == "y":
            break
        elif answer == "n":
            break
        else:
            continue
     
    # continue calculation?    
    if answer == "y":
        continue
    else:
        break
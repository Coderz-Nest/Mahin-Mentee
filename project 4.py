#Number Converter: Create a program that can convert numbers between different number systems,
# such as  binary, decimal, and hexadecimal

def den_to_bin(num):
    binary=""
    while True:
        if num>1:
            rem = num % 2
            binary += str(rem)
            num = num // 2
        elif num==1:
            binary += str(0)
            break
        else:
            binary += str(1)
            break
    print(binary)
    return str(binary[::-1])



print(str(den_to_bin(567)))



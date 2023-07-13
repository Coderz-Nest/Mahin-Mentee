#make the decimal to hexadecimal function

def den_to_hex(num):
    hexadecimal=""
    hex_list=['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    while True:
        if num>15:
            rem = num % 16
            hexadecimal += hex_list[rem -1]
            num = num // 16

        else:
            hexadecimal += hex_list[rem - 1]
            break
    return str(hexadecimal[::-1])

print(str(den_to_hex(4456)))



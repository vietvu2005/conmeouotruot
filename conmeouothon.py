def ehehe(password): # encode password function
    encode = ''
    for char in password:
        encoded_char = chr(ord(char) + 1)
        encode += encoded_char
    return encode

def main():
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
        option = int(input('Please enter an option: '))
        if option == 3:
            break
        else:
            password = input('Please enter your password to encode: ')
            if option == 1:
                encode = ehehe(password)
                print('Your password has been encoded and stored!')
            elif option == 2:
                print(f'The encoded password is {encode}, and the original password is {password}.')

if __name__ == '__main__':
    main()
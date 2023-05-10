alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def crypt(input_text, shift_amount, choice):
    if choice == "encode":
        cipher_text = ""
        for letter in input_text:
            try:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                new_letter = alphabet[new_position]
                cipher_text += new_letter
            except ValueError:
                cipher_text += letter
        print(f"The encoded text is {cipher_text}")
    if choice == "decode":
        plain_text = ""
        for letter in input_text:
            try:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                new_letter = alphabet[new_position]
                plain_text += new_letter
            except ValueError:
                plain_text += letter
        print(f"The decoded text is {plain_text}")
    if not choice == "decode" and not choice == "encode":
        print("Invalid choice!")


run = True
greet = ''' _____                                 _       _               
/  __ \                               (_)     | |              
| /  \/ ___  __ _ ___  ___ _ __    ___ _ _ __ | |__   ___ _ __ 
| |    / _ \/ _` / __|/ _ \ '__|  / __| | '_ \| '_ \ / _ \ '__|
| \__/\  __/ (_| \__ \  __/ |    | (__| | |_) | | | |  __/ |   
 \____/\___|\__,_|___/\___|_|     \___|_| .__/|_| |_|\___|_|   
                                        | |                    
                                        |_|                    

'''
print(greet)
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    crypt(input_text=text, shift_amount=shift, choice=direction)
    answer = input(print("Run again? (Y/N)")).lower()
    if answer == "n" or "no":
        run = False
    else:
        run

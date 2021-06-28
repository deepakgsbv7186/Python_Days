alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input("Type your message: ").lower()
shift = int(input("Type the shift number: "))

#TODO-1: Create a different function called 'decrypt' that takes the 'text'
#  and 'shift' as inputs.
  #TODO-2: Inside the 'decrypt' function, shift each letter
  #  of the 'text' *backwards* in the alphabet by the shift amount 
  # and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
def cipher(input_text, shift_amount, given_direction):
    your_text = ""
    len_apha = len(alphabet)
    if shift_amount > len_apha:
        shift_amount %= len_apha
    if given_direction == "decode":
        shift_amount *= -1
    for i in range(len(input_text)):
        fount_at_index = alphabet.index(input_text[i])
        new_position = shift_amount + fount_at_index
        if new_position > (len_apha - 1):
            your_text += alphabet[new_position % len_apha]
        else:
            your_text += alphabet[new_position]
    print(f"Here's {direction}d result: {your_text}")        

#TODO-3: Check if the user wanted to encrypt or decrypt 
# the message by checking the 'direction' variable.
#  Then call the correct function based on that 'drection' variable.
#  You should be able to test the code to encrypt *AND* decrypt a message.
# if direction != "encode" or direction != "decode":
#     print("Bad Entry")   
# else:
#     cipher(input_text=text,shift_amount=shift,given_direction=direction)
cipher(input_text=text,shift_amount=shift,given_direction=direction)
import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
choice=''
while choice!='no':
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  def caesar(text,shift,direction):
    cipher_text=''
    for letter in text:
      if not letter in alphabet:
        cipher_text=cipher_text+letter
        continue

      if direction=='encode':
        index=alphabet.index(letter)+shift
      elif direction=='decode':
        index=alphabet.index(letter)-shift
      cipher_text+=alphabet[index]
    print(f'The {direction}d message is {cipher_text}')
      
  caesar(text,shift%26,direction)
  choice=input("\nType 'yes' if you want to go again. Otherwise type 'no' : ")
  if choice=='no':
    print('Good Bye')

  
# Challange 1

# def encrypt(text ,shift):
#   cipher_text=''
#   for letter in text:
#     index=alphabet.index(letter)+shift
#     cipher_text+=alphabet[index]
#   print(f'The encoded message is {cipher_text}')
  
# def decrypt(text ,shift):
#   cipher_text=''
#   for letter in text:
#     index=alphabet.index(letter)-shift
#     cipher_text+=alphabet[index]
#   print(f'The decoded message is {cipher_text}')

# if direction=='encode':
#   encrypt(text,shift)
# elif direction=='decode':
#   decrypt(text,shift)
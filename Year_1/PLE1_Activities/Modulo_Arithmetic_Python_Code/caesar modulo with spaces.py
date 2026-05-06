#Caesar cipher with modulo arithmetic

alphabet = [ 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#index   = [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25 ]

print("Enter your phrase:")
phrase = input()
print("Enter a key shift, by choosing a number between 1-25")
keyshift = int(input())

cipher_list = []

for i in phrase:
    if i == " ":
        cipher_list.append(" ")
    else:   
        index_position = alphabet.index(i)
        cipher_index = (index_position + keyshift) % 26
        cipher_list.append(alphabet[cipher_index])

ciphertext = "".join(cipher_list)

#print(cipher_list)
print(ciphertext)


    

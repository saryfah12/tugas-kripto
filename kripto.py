key = input('masukan Key: ')
byte_input = bytes(key, 'utf-8')
plaintext = input('Masukan Plainteks: ')

encrypted_data = b''
encrypted_data.decode('biner')


for i, c in enumerate(plaintext):
    encrypted_data += bytes([ord(c) ^ byte_input[i % len(byte_input)]])
print('hasil enkripsi: ', encrypted_data.decode('utf-8'))


def decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += chr(ord(encrypted_text[i]) ^ ord(key[i % len(key)]))
    return decrypted_text


encrypted_text = encrypted_data.decode('utf-8')
decrypted_text = decrypt(encrypted_text, key)


print('hasil Dekripsi: ', decrypted_text)


def file_data(filename):
    with open(filename, 'r') as f:
        data = ' '.join(f.readlines())
    return data

def add_chars(a, b):
    c = ord(a) - ord("A")
    d = ord(b) - ord("A")
    bounded = (c + d) % 26
    return chr(bounded + ord("A"))

def subtract_chars(small, large):
    c = ord(small) - ord("A")
    d = ord(large) - ord("A")
    bounded =  (d - c) % 26
    return chr(bounded + ord("A"))

def cipher_char(key, plain):
    return add_chars(key, plain)

def decipher_char(key, cipher):
    return subtract_chars(small=key, large=cipher)

def get_key_char_generator(key):
    def get_key_mod_char(i):
        return key[i % len(key)] 
    return get_key_mod_char

def is_char(c):
    return ord('A') <= ord(c) <= ord("Z")

def decipher_text(ciphertext, key):
    get_key_char = get_key_char_generator(key)

    safetext = ''.join(filter(is_char, ciphertext))
    plaintext = ''.join(decipher_char(get_key_char(i), c) for i, c in enumerate(safetext))
    
    return plaintext

def generate_ciphertext(plaintext, key):
    get_key_char = get_key_char_generator(key)

    safetext = ''.join(filter(is_char, plaintext))
    ciphertext = ''.join(cipher_char(get_key_char(i), c) for i, c in enumerate(safetext))
    
    return ciphertext

def readable(text):
    l = [c for c in text]
    for i in range(len(text)-(len(text)%4), 0, -4):
        l.insert(i, ' ')
    return ''.join(l)

if __name__ == "__main__": 
    plaintext = file_data("plaintext.txt").upper()
    key = file_data("key.txt").upper()

    ciphertext = generate_ciphertext(plaintext, key)
    with open("ciphertext.txt", 'w+') as f:
        f.write(readable(ciphertext))
    
    # # DEBUG / Test
    # new_plain = decipher_text(ciphertext, key)
    # print(new_plain)


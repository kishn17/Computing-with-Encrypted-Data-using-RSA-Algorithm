import math

# Encryption alphabet
alphabet_e = {
    'a': '01', 'b': '02', 'c': '03', 'd': '04', 'e': '05',
    'f': '06', 'g': '07', 'h': '08', 'i': '09', 'j': '10',
    'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15',
    'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20',
    'u': '21', 'v': '22', 'w': '23', 'x': '24', 'y': '25',
    'z': '26', ' ': '32'
}

# Decryption alphabet
alphabet_d = {n: c for c, n in alphabet_e.items()}

# Euclidean Algorithm: Find GCD of two numbers
def gcd(a, b):
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)

# Extended Euclidean Algorithm: Find Multiplicative Inverse
def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate encryption keys, e, and d
def generate_keys(p, q):
    n = p * q
    N0 = (p - 1) * (q - 1)
    for i in range(2, N0):
        if gcd(i, N0) == 1:
            e = i
            break
    d = modinv(e, N0)
    return n, e, d

# Encrypt character
def encrypt(char, N, e):
    return str((int(char) ** e) % N).zfill(2)

# Decrypt character
def decrypt(char, N, d):
    return str((int(char) ** d) % N).zfill(2)

# Split word into characters
def split(word):
    return [char for char in word]

# Encrypt message
def encrypt_message(msg, N, e):
    plaintext = msg.lower().split()
    encrypted = []
    for word in plaintext:
        chars = split(word)
        encrypted_chars = [encrypt(alphabet_e[char], N, e) for char in chars]
        encrypted_word = " ".join(encrypted_chars)
        encrypted.append(encrypted_word)
    encrypted = f" {encrypt(alphabet_e[' '], N, e)} ".join(encrypted)
    return encrypted

# Decrypt message
def decrypt_message(msg, N, d):
    encrypted = msg.split()
    decrypted = []
    plaintext = []
    for char in encrypted:
        decrypted.append(decrypt(char, N, d))
    for char in decrypted:
        plaintext.append(alphabet_d[char])
    plaintext = "".join(plaintext)
    return plaintext

# Option Menu
def options():
    print("Options:\n\
    0 - Generate Key Pair\n\
    1 - Encrypt message from file\n\
    2 - Decrypt message from file\n\
    3 - Encrypt message in terminal\n\
    4 - Decrypt message in terminal\n")

# User interface
while True:
    options()
    selection = input("Enter your choice: ")

    # Generate key pair
    if selection == "0":
        try:
            p = int(input("Enter the first prime number: "))
            q = int(input("Enter the second prime number: "))
            if not (is_prime(p) and is_prime(q)):
                raise ValueError("Both numbers must be prime.")
            N, e, d = generate_keys(p, q)
            print(f"Public key:\nN: {N}\ne: {e}\n")
            print(f"Private key:\nN: {N}\nd: {d}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")
    
    # Encrypt message from file
    elif selection == "1":
        try:
            N = int(input("Enter public key N: "))
            e = int(input("Enter public key e: "))
            with open("input.txt", "r") as fin:
                message = fin.read()
            with open("encrypted.txt", "w") as fout:
                fout.write(encrypt_message(message, N, e))
            print("File encrypted!\n")
        except Exception as ex:
            print(f"Error: {ex}\n")
    
    # Decrypt message from file
    elif selection == "2":
        try:
            N = int(input("Enter private key N: "))
            d = int(input("Enter private key d: "))
            with open("input.txt", "r") as fin:
                message = fin.read()
            with open("decrypted.txt", "w") as fout:
                fout.write(decrypt_message(message, N, d))
            print("File decrypted!\n")
        except Exception as ex:
            print(f"Error: {ex}\n")
    
    # Encrypt message in terminal
    elif selection == "3":
        try:
            N = int(input("Enter public key N: "))
            e = int(input("Enter public key e: "))
            message = input("Enter message to encrypt:\n")
            print(f"\nEncrypted message:\n{encrypt_message(message, N, e)}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")
    
    # Decrypt message in terminal
    elif selection == "4":
        try:
            N = int(input("Enter private key N: "))
            d = int(input("Enter private key d: "))
            message = input("Enter message to decrypt:\n")
            print(f"\nDecrypted message:\n{decrypt_message(message, N, d)}\n")
        except Exception as ex:
            print(f"Error: {ex}\n")
    
    # Invalid selection
    else:
        print("Invalid choice\n")
    
    # Option to exit
    exit_choice = input("Make another selection?\n'Y' to continue\nany other key to exit\n").upper()
    print()
    if exit_choice != "Y":
        break

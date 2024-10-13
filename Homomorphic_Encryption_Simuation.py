import numpy as np

class SimpleHomomorphicEncryption:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        # Simple encryption by adding the key
        return plaintext + self.key

    def decrypt(self, ciphertext):
        # Simple decryption by subtracting the key
        return ciphertext - self.key

    def add(self, ciphertext1, ciphertext2):
        # Homomorphic addition
        return ciphertext1 + ciphertext2

    def multiply(self, ciphertext, scalar):
        # Homomorphic multiplication (only with a scalar for simplicity)
        return ciphertext + (scalar * self.key)

class InMemoryDatabase:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def retrieve(self, key):
        return self.data.get(key)

# Simulation
def main():
    # Initialize the encryption system with a simple key
    key = 10
    homomorphic_encryption = SimpleHomomorphicEncryption(key)

    # Initialize in-memory database
    db = InMemoryDatabase()

    # Insert encrypted values into the database
    for i in range(1, 4):
        encrypted_value = homomorphic_encryption.encrypt(i)
        db.insert(f'record_{i}', encrypted_value)

    # Retrieve and perform operations on encrypted data
    encrypted_sum = 0
    for i in range(1, 4):
        encrypted_value = db.retrieve(f'record_{i}')
        print(f'Encrypted value of record_{i}: {encrypted_value}')
        encrypted_sum = homomorphic_encryption.add(encrypted_sum, encrypted_value)

    # Decrypt the final sum
    decrypted_sum = homomorphic_encryption.decrypt(encrypted_sum)
    print(f'Decrypted sum: {decrypted_sum}')  # Should output 6 (1 + 2 + 3)

if __name__ == "__main__":
    main()

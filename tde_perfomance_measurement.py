import time
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher = Fernet(key)

# Sample data to encrypt
data = b"This is a sensitive message that need to be encryped."

# Measure encryption time
start_encryption_time = time.time()
encrypted_data = cipher.encrypt(data)
end_encryption_time = time.time()
encryption_time = end_encryption_time - start_encryption_time

# Measure decryption time
start_decryption_time = time.time()
decrypted_data = cipher.decrypt(encrypted_data)
end_decryption_time = time.time()
decryption_time = end_decryption_time - start_decryption_time

# Output the results
print(f"Original Data: {data}")
print(f"Encrypted Data: {encrypted_data}")
print(f"Decrypted Data: {decrypted_data}")
print("")
print(f"Time taken to encrypt: {encryption_time:.6f} seconds")
print(f"Time taken to decrypt: {decryption_time:.6f} seconds")

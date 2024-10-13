import psutil
import os
import time
from cryptography.fernet import Fernet

#  Memory Consumption Measurement
process = psutil.Process(os.getpid())
mem_before = process.memory_info().rss  # Memory in bytes before execution

#  Latency Overhead Measurement
start_time = time.perf_counter()    
# start_time = time.time()
#  -----------------------------------------------------Performace measurement file---------------------
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

# -----------------------------------------------------------EOF---------------------------------------
# Execute your homomorphic encryption code here

mem_after = process.memory_info().rss  # Memory in bytes after execution
print(f"Memory consumed: {mem_after - mem_before} bytes")

# end_time = time.time()
# print(f"Latency: {end_time - start_time} seconds")
end_time = time.perf_counter()
print(f"Latency: {end_time - start_time} seconds")
    
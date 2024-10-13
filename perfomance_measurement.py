import time
import Homomorphic_Encryption_Simuation

def measure_performance():
    # Initialize the encryption system
    key = 5
    homomorphic_encryption = Homomorphic_Encryption_Simuation.SimpleHomomorphicEncryption(key)

    # Test data size
    data_size = 100000
    encrypted_values = []

    # Measure encryption time
    start_time = time.time()
    for i in range(1, data_size + 1):
        encrypted_value = homomorphic_encryption.encrypt(i)
        encrypted_values.append(encrypted_value)
    encryption_time = time.time() - start_time
    print(f'Encryption time for {data_size} records: {encryption_time:.4f} seconds')

    # Measure addition time
    encrypted_sum = 0
    start_time = time.time()
    for value in encrypted_values:
        encrypted_sum = homomorphic_encryption.add(encrypted_sum, value)
    addition_time = time.time() - start_time
    print(f'Addition time for {data_size} records: {addition_time:.4f} seconds')

    # Measure decryption time
    start_time = time.time()
    decrypted_sum = homomorphic_encryption.decrypt(encrypted_sum)
    decryption_time = time.time() - start_time
    print(f'Decryption time: {decryption_time:.4f} seconds')

if __name__ == "__main__":
    measure_performance()

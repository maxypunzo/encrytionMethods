from cryptography.fernet import Fernet
import json

class InMemoryDatabase:
    def __init__(self, key=None):
        # Generate a key if none is provided
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)
        self.data_store = {}

    def encrypt_data(self, data):
        """Encrypt data before storing it."""
        json_data = json.dumps(data).encode('utf-8')
        encrypted_data = self.cipher.encrypt(json_data)
        print("Encrypted Data At Rest:", encrypted_data)
        print(" ")
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypt data when retrieving it."""
        decrypted_data = self.cipher.decrypt(encrypted_data)
        return json.loads(decrypted_data)

    def insert(self, key, value):
        """Insert data into the in-memory database."""
        encrypted_value = self.encrypt_data(value)
        self.data_store[key] = encrypted_value

    def retrieve(self, key):
        """Retrieve data from the in-memory database."""
        encrypted_value = self.data_store.get(key)
        if encrypted_value is None:
            return None
        return self.decrypt_data(encrypted_value)

# Example usage
if __name__ == "__main__":
    # Create an in-memory database
    db = InMemoryDatabase()

    # Insert some data
    db.insert("user1", {"name": "Alice", "age": 30})
    db.insert("user2", {"name": "Bob", "age": 25})

    # Retrieve data
    user1 = db.retrieve("user1")
    user2 = db.retrieve("user2")

    print("Retrieved User 1:", user1)
    print("Retrieved User 2:", user2)

    # Attempt to retrieve a non-existent user
    user3 = db.retrieve("user3")
    print("Retrieved User 3:", user3)  # Should be None

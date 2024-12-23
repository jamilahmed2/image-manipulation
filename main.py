from PIL import Image
import numpy as np

# Function to encrypt the image
def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixel_array = np.array(image)
        
        # Encrypt by applying a mathematical operation (e.g., XOR with key)
        encrypted_array = pixel_array ^ key
        
        # Swap rows and columns for additional encryption
        encrypted_array = np.rot90(encrypted_array)
        
        encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
        encrypted_image.save(output_path)
        print(f"Image successfully encrypted and saved as {output_path}.")
    except Exception as e:
        print(f"Error encrypting image: {e}")

# Function to decrypt the image
def decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path)
        pixel_array = np.array(image)

        # Reverse the rotation
        decrypted_array = np.rot90(pixel_array, -1)
        
        # Decrypt by reversing the mathematical operation
        decrypted_array = decrypted_array ^ key

        decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
        decrypted_image.save(output_path)
        print(f"Image successfully decrypted and saved as {output_path}.")
    except Exception as e:
        print(f"Error decrypting image: {e}")

# Main program
def main():
    print("Welcome to the Image Encryption Tool")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        input_path = input("Enter the path to the input image: ")
        output_path = input("Enter the path to save the encrypted image: ")
        key = int(input("Enter a numeric encryption key (e.g., 123): "))
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        input_path = input("Enter the path to the encrypted image: ")
        output_path = input("Enter the path to save the decrypted image: ")
        key = int(input("Enter the numeric key used for encryption: "))
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

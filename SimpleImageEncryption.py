from PIL import Image
import numpy as np

def create_sample_image(image_path):
    # Image dimensions
    width, height = 100, 100
    
    # Generate random pixel data
    pixels = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    
    # Create a new image from the pixel data
    img = Image.fromarray(pixels, 'RGB')
    
    # Save the image
    img.save(image_path)
    print(f"Sample image saved as {image_path}")

def encrypt_image(input_path, output_path):
    # Open the image
    img = Image.open(input_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Encrypt the image by inverting the pixel values (simple XOR with 255)
    encrypted_array = 255 - img_array
    
    # Convert the numpy array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save(output_path)
    print(f"Encrypted image saved as {output_path}")

def decrypt_image(input_path, output_path):
    # Open the encrypted image
    img = Image.open(input_path)
    
    # Convert image to numpy array
    img_array = np.array(img)
    
    # Decrypt the image by inverting the pixel values back (simple XOR with 255)
    decrypted_array = 255 - img_array
    
    # Convert the numpy array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save(output_path)
    print(f"Decrypted image saved as {output_path}")

# Create a sample image
create_sample_image('input_image.png')

# Encrypt the sample image
encrypt_image('input_image.png', 'encrypted_image.png')

# Decrypt the encrypted image
decrypt_image('encrypted_image.png', 'decrypted_image.png')


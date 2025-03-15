import os

def delete_image(filepath):
  """Deletes an image file.

  Args:
    filepath: The path to the image file.
  """
  try:
    os.remove(filepath)
    print(f"Image '{filepath}' deleted successfully.")
  except FileNotFoundError:
    print(f"Error: Image '{filepath}' not found.")
  except PermissionError:
    print(f"Error: Permission denied to delete '{filepath}'.")
  except OSError as e: #Catch any other OS related errors.
      print(f"Error deleting '{filepath}': {e}")

if __name__ == "__main__" :
    # # Example usage (replace with your actual image file path):
    image_path = "equation_images/savedimage.jpg" # Example filename.

    # Create a dummy image file for demonstration (replace with your actual image creation logic)

    try:
        with open(image_path, "wb") as f:
            f.write(b"dummy image data") #replace with actual image data.
        print(f"Dummy image '{image_path}' created.")
        delete_image(image_path)

    except Exception as e:
        print(f"An error occured creating or deleting the sample image file: {e}")

    # #Example usage with a file that does not exist.
    # delete_image("nonexistent_image.jpg")
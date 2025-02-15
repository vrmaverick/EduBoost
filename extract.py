import tarfile

def extract_tgz(file_path, output_dir):
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=output_dir)
        print(f"Extracted '{file_path}' to '{output_dir}'")

# Example usage
extract_tgz("./data/mathwriting-2024.tgz", "./data/mathwriting-2024")

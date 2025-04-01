def read_file(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error reading file: {e}"

def write_temp_path(path):
    with open(r"work\temp\temp_info.txt", "w") as f:
        f.write(path)
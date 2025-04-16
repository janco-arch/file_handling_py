

def read_file(file_path):git 
    """Reads the content of a file """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def modify_content(content):
    """Modifies the content of the file. 
    converts the content to uppercase."""
    return content.upper()

def write_file(file_path, content):
    """Writes the modified content to a new file."""
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    input_file = input("Please enter the path to the input file: ")  # Ask user for input file path
    output_file = 'output.txt'  

    
    content = read_file(input_file)
    if content is None:
        return  

    # Modify the content
    modified_content = modify_content(content)

    
    write_file(output_file, modified_content)

    print(f"Modified content has been written to {output_file}")

if __name__ == "__main__":
    main()

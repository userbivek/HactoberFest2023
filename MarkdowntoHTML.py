import markdown
import os

def convert_markdown_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as md_file:
            markdown_text = md_file.read()
            html = markdown.markdown(markdown_text)
            with open(output_file, 'w', encoding='utf-8') as html_file:
                html_file.write(html)
            print(f"Conversion of {input_file} to {output_file} completed successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def convert_multiple_markdown_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for file in os.listdir(input_directory):
        if file.endswith(".md"):
            input_path = os.path.join(input_directory, file)
            output_file = os.path.join(output_directory, os.path.splitext(file)[0] + ".html")
            convert_markdown_file(input_path, output_file)

if __name__ == "__main__":
    input_file = "input.md"
    output_file = "output.html"
    
    # Single file conversion
    convert_markdown_file(input_file, output_file)
    
    input_directory = "markdown_files"
    output_directory = "html_files"
    
    # Batch conversion for all .md files in a directory
    convert_multiple_markdown_files(input_directory, output_directory)

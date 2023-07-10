import re
import os


def replace_commas_with_dot(file_path):
    output_lines = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                modified_line = re.sub(r'(\d+),(\d+)', r'\1.\2', line)
                output_lines.append(modified_line.strip())
            else:
                output_lines.append('')  

    return '\n'.join(output_lines)



input_file_path = 'replace.txt' 
output_file_path = os.path.join(os.path.dirname(input_file_path), 'rates.txt')
modified_content = replace_commas_with_dot(input_file_path)

with open(output_file_path, 'w') as output_file:
    output_file.write(modified_content)

print(f"Modified content saved to {output_file_path}")

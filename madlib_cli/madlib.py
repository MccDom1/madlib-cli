# madlib.py

import re

def welcome_message():
    print("Welcome to the Madlib game! Follow the prompts to create your own Madlib story.")

def read_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_template(template):
    # Use regular expression to find placeholders in the template
    placeholders = re.findall(r'\{(.*?)\}', template)
    
    # Replace placeholders with empty curly braces in the stripped template
    stripped_template = re.sub(r'\{(.*?)\}', '{}', template)

    return stripped_template, placeholders

# Modify the merge function in madlib.py
def merge(template, parts):
    return template.format(*parts)



def get_user_inputs(placeholders):
    inputs = {}
    for placeholder in placeholders:
        user_input = input(f"Enter a {placeholder}: ")
        inputs[placeholder] = user_input
    return inputs

def populate_template(template, inputs):
    return template.format(**inputs)

def display_completed_madlib(completed_madlib):
    print("\nYour completed Madlib:\n")
    print(completed_madlib)

def write_to_file(completed_madlib, output_file):
    with open(output_file, 'w') as file:
        file.write(completed_madlib)

if __name__ == "__main__":
    # Define the file paths
    template_file = "template.txt"  # Update with your actual template file
    output_file = "completed_madlib.txt"  # Update with your desired output file

    # Step 1: Welcome message
    welcome_message()

    # Step 2: Read template and parse placeholders
    template_content = read_template(template_file)
    placeholders = parse_template(template_content)

    # Step 3: Get user inputs for placeholders
    user_inputs = get_user_inputs(placeholders)

    # Step 4: Populate template with user inputs
    completed_madlib = populate_template(template_content, user_inputs)

    # Step 5: Display completed Madlib to the user
    display_completed_madlib(completed_madlib)

    # Step 6: Write completed Madlib to a new file
    write_to_file(completed_madlib, output_file)

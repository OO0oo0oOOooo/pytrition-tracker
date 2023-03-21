import os
from datetime import datetime
import tkinter as tk

now = datetime.now()
year_month = now.strftime('%Y-%m')
day = now.strftime('%d')

directory = os.path.join(os.getcwd(), year_month)

file_template = f'Template.txt'
file_template_path = os.path.join(os.getcwd(), file_template)

file_name = f'nut-{day}.txt'
file_path = os.path.join(directory, file_name)

def create_file():
    if not os.path.exists(directory):
        os.makedirs(directory)

    if not os.path.exists(file_template_path):
        with open(file_template_path, 'w') as f:
            f.write('Calories: 0\nProtein: 0\nFat: 0\n\n\nC:0\nP:0\nF:0\n\n\nC:0\nP:0\nF:0\n\n\nC:0\nP:0\nF:0')
    
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:

            with open(file_template_path, 'r') as other_file:
                f.write(other_file.read())

def calc_nutrition():
    total_calories = 0
    total_protein = 0
    total_fat = 0

    # Open file in read-write mode and parse lines
    with open(file_path, 'r+') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('C:'):
                calories = int(line.split('C:')[1])
                total_calories += calories

            elif line.startswith('P:'):
                protein = int(line.split('P:')[1])
                total_protein += protein

            elif line.startswith('F:'):
                fat = int(line.split('F:')[1])
                total_fat += fat

        # Write new total calories back to file
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.startswith('Calories:'):
                f.write(f'Calories: {total_calories}\n')
            elif line.startswith('Protein:'):
                f.write(f'Protein: {total_protein}\n')
            elif line.startswith('Fat:'):
                f.write(f'Fat: {total_fat}\n')
            else:
                f.write(line)

create_file();

root = tk.Tk()
root.title('Cal Counter')

button_parse_file = tk.Button(root, text='Calc Nutrition', command=calc_nutrition)
button_parse_file.pack()

label_result = tk.Label(root)
label_result.pack()

root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter.font import Font  # Import the Font class

root = Tk()
root.title = "Deutsch Test"
root.geometry("800x600")

# Set up the frame
frm = ttk.Frame(root, padding=10)
frm.grid()

with open("answers.txt", "w") as f:
    f.write("")
    f.close()

# Define a font
custom_font = Font(family="JetBrains Mono Nerd Font", size=14)

style = ttk.Style()
style.configure("Custom.TCheckbutton", font=custom_font)

text = [
    "Lies den Textabschnitt : markiere alle richtige Antworte\n",
    "Jana ist 15 Jahre alt und kommt aus Deutschland.\n",
    "Im letzten Sommer hat sie an einer Sprachreise nach England teilgenommen.\n",
    "Sie wollte ihr Englisch verbessern und neue Leute kennenlernen.\n",
    "Die Sprachreise dauerte zwei Wochen und war ein großes Erlebnis  für sie.\n",
    "Jeden Morgen hatte Jana Sprachunterricht in einer kleinen Gruppe.\n",
    "Der Unterricht war interessant und die Lehrer waren sehr freundlich.\n",
    "(3 Points)"
]

options = [
    "Jana macht eine Sprachreise\n",
    "Jana war in England 14 Tage.\n",
    "Jana hatte am Vormittag die Unterrichte.\n",
    "Die Unterrichte waren langweilig\n",
    "Janas Lehrer waren sehr freundlich\n"
]

# Apply the font to the Label
ttk.Label(frm, text="".join(i for i in text),font=custom_font).grid(column=0, row=0)

# Variables to track selected answers
selected_vars = {option: BooleanVar() for option in options}

# Function to enforce a maximum of 3 selections
def toggle_checkbutton(option):
    # Count the current number of selected answers
    selected_count = sum(var.get() for var in selected_vars.values())
    if selected_count > 3:
        # If more than 3 are selected, uncheck the most recent one
        selected_vars[option].set(False)

# Create checkbuttons for each option
for idx, option in enumerate(options):
    checkbutton = ttk.Checkbutton(
        frm,
        text=option,
        style="Custom.TCheckbutton",
        variable=selected_vars[option],
        command=lambda opt=option: toggle_checkbutton(opt)
    )
    checkbutton.grid(column=0, row=idx + 1, sticky=W, padx=20, pady=5)

def submit():
    with open("answers.txt", "a") as f:
        # Write only selected answers to the file
        for option, var in selected_vars.items():
            if var.get():  # Check if this option was selected
                f.write(option)
    root.destroy()  # Close the window after saving answers

ttk.Button(frm, text="Submit", command=submit).grid(column=0, row=len(options) + 1, pady=20)

root.mainloop()

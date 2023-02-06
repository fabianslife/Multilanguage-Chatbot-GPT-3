import tkinter as tk

def set_language(language):
    global selected_language
    selected_language = language
    print(f"Selected language: {selected_language}")

root = tk.Tk()
root.title("Select your language")

selected_language = None

header = tk.Label(root, text="Select your language", font=("Helvetica", 16))
header.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

languages = ["English", "French", "German", "Italian", "Spanish",
             "Swedish", "Finnish", "Dutch", "Polish", "Czech",
             "Greek", "Hungarian", "Chinese", "Japanese", "southKorean"]

scrollbar = tk.Scrollbar(root, orient="vertical")
scrollbar.grid(row=1, column=5, rowspan=5, sticky="ns")

canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
canvas.grid(row=1, column=0, rowspan=5, columnspan=5)
scrollbar.config(command=canvas.yview)

for i, language in enumerate(languages):
    row = i // 4 + 1
    col = i % 4
    flag = tk.PhotoImage(file=f"/Users/fabian/Documents/GPT-3_Ada/gui/{language.lower()}_flag.png")
    button = tk.Button(canvas, image=flag, relief="groove", highlightbackground="#f2f2f2", highlightcolor="#dddddd", command=lambda language=language: set_language(language))
    canvas.create_window((col * 110 + 10, row * 60 + 10), window=button, anchor="nw")

canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()
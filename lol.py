import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Abas em Tkinter")

notebook = ttk.Notebook(root)
notebook.pack(pady=10, padx=10, expand=True, fill="both")

# Criar a primeira aba
frame1 = ttk.Frame(notebook)
notebook.add(frame1, text='Aba 1')
tk.Label(frame1, text="Conteúdo da Aba 1").pack(pady=20)

# Criar a segunda aba
frame2 = ttk.Frame(notebook)
notebook.add(frame2, text='Aba 2')
tk.Label(frame2, text="Conteúdo da Aba 2").pack(pady=20)

root.mainloop()
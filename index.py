import tkinter as tk

# Banco de dados simulado para usuários
database = {
    'usuario1': 'senha1',
    'usuario2': 'senha2',
    'usuario3': 'senha3'
}

def fazer_login():
    username = username_entry.get()
    password = password_entry.get()

    # Verifica se o usuário existe no banco de dados e a senha está correta
    if username in database and database[username] == password:
        result_label.config(text="Login bem-sucedido!", fg="green")
    else:
        result_label.config(text="Credenciais inválidas.", fg="red")

# Cria a janela
window = tk.Tk()
window.title("Sistema de Login")
window.geometry("300x200")  # Define as dimensões da janela

# Cria os widgets
username_label = tk.Label(window, text="Nome de usuário:", font=("Arial", 12))
username_entry = tk.Entry(window, font=("Arial", 12))
password_label = tk.Label(window, text="Senha:", font=("Arial", 12))
password_entry = tk.Entry(window, show="*", font=("Arial", 12))
login_button = tk.Button(window, text="Login", command=fazer_login, font=("Arial", 12), bg="blue", fg="white")
result_label = tk.Label(window, text="", font=("Arial", 12))

# Posiciona os widgets na janela
username_label.pack(pady=10)
username_entry.pack()
password_label.pack(pady=10)
password_entry.pack()
login_button.pack(pady=10)
result_label.pack()

# Inicia o loop principal da janela
window.mainloop()

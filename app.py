import tkinter as tk

root = tk.Tk()
root.title("Регистрация и авторизация")
root.geometry("640x480")
root.configure(background='#B5D5CA')


def registration_form():
    reg_window = tk.Toplevel(root)
    reg_window.title("Форма регистрации")
    reg_window.geometry("640x480")
    reg_window.configure(background='#B5D5CA')
    email_label = tk.Label(reg_window, text="Email:")
    email_label.configure(bg="#D1EEFC")
    email_entry = tk.Entry(reg_window)
    email_entry.configure(bg="#FFFCD6")
    pass_label = tk.Label(reg_window, text="Пароль:")
    pass_label.configure(bg="#D1EEFC")
    pass_entry = tk.Entry(reg_window, show="*")
    pass_entry.configure(bg="#FFFCD6")
    role_label = tk.Label(reg_window, text="Ваша роль:")
    role_label.configure(bg="#D1EEFC")
    role_options = ["Заказчик", "Менеджер", "Кладовщик", "Дирекция"]
    role_var = tk.StringVar(reg_window)
    role_var.set(role_options[0])
    role_dropdown = tk.OptionMenu(reg_window, role_var, *role_options)
    register_btn = tk.Button(reg_window, text="Зарегистрироваться", command=lambda: print("Регистрация прошла успешно"))
    register_btn.configure(bg="#E0AFA9")
    email_label.pack()
    email_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    role_label.pack()
    role_dropdown.pack()
    register_btn.pack()


# Функция для создания формы авторизации
def login_form():
    login_window = tk.Toplevel(root)
    login_window.title("Форма авторизации")
    login_window.geometry("640x480")
    login_window.configure(background='#B5D5CA')
    email_label = tk.Label(login_window, text="Email:")
    email_entry = tk.Entry(login_window)
    pass_label = tk.Label(login_window, text="Пароль:")
    pass_entry = tk.Entry(login_window, show="*")
    login_btn = tk.Button(login_window, text="Войти", command=lambda: print("Авторизация прошла успешно"))
    login_btn.configure(bg="#E0AFA9")
    email_label.pack()
    email_entry.pack()
    pass_label.pack()
    pass_entry.pack()
    login_btn.pack()


registration_btn = tk.Button(root, text="Регистрация", command=registration_form)
registration_btn.configure(bg="#E0AFA9")
login_btn = tk.Button(root, text="Уже зарегистрированы? Войдите в аккаунт", command=login_form)
login_btn.configure(bg="#E0AFA9")

registration_btn.pack(pady=50)
login_btn.pack()

root.mainloop()

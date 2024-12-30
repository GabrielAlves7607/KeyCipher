from tkinter.filedialog import asksaveasfilename
from tkinter import PhotoImage
import tkinter as tk
from tkinter import messagebox

# Dicionários de codificação e decodificação
codificacao = {
    'a': 'q', 'b': 'g', 'c': 'd', 'd': 'e', 'e': '3', 'f': 'r', 'g': 't', 'h': 'y', 'i': '8', 'j': 'u',
    'k': 'i', 'l': 'o', 'm': 'j', 'n': 'h', 'o': '9', 'p': '0', 'q': '1', 'r': '4', 's': 'w', 't': '5',
    'u': '7', 'v': 'f', 'w': '2', 'x': 's', 'y': '6', 'z': 'a'
}


decodificacao = {
    'q': 'a', 'g': 'b', 'd': 'c', 'e': 'd', '3': 'e', 'r': 'f', 't': 'g', 'y': 'h', '8': 'i', 'u': 'j',
    'i': 'k', 'o': 'l', 'j': 'm', 'h': 'n', '9': 'o', '0': 'p', '1': 'q', '4': 'r', 'w': 's', '5': 't',
    '7': 'u', 'f': 'v', '2': 'w', 's': 'x', '6': 'y', 'a': 'z'
}


def criptografar(mensagem):
    return ''.join(codificacao.get(char, char) for char in mensagem.lower())


def descriptografar(mensagem):
    return ''.join(decodificacao.get(char, char) for char in mensagem.lower())


def executar_criptografia():
    mensagem = entrada.get()
    if not mensagem:
        messagebox.showwarning("Aviso", "Por favor, insira uma mensagem para criptografar.")
        return
    resultado = criptografar(mensagem)
    saida.config(state="normal")
    saida.delete("1.0", tk.END)
    saida.insert("1.0", resultado)
    saida.config(state="disabled")
    msg_usuario.config(text="Mensagem criptografada com sucesso!", fg="#4caf50")


def executar_descriptografia():
    mensagem = entrada.get()
    if not mensagem:
        messagebox.showwarning("Aviso", "Por favor, insira uma mensagem para descriptografar.")
        return
    resultado = descriptografar(mensagem)
    saida.config(state="normal")
    saida.delete("1.0", tk.END)
    saida.insert("1.0", resultado)
    saida.config(state="disabled")
    msg_usuario.config(text="Mensagem descriptografada com sucesso!", fg="#4caf50")


def salvar_arquivo():
    texto = saida.get("1.0", tk.END).strip()  # Pega o conteúdo da saída e remove espaços extras
    if not texto:
        messagebox.showwarning("Aviso", "Não há nada para salvar.")
        return

    caminho_arquivo = asksaveasfilename(defaultextension=".txt", 
                                        filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")],
                                        title="Salvar Mensagem")
    if caminho_arquivo:  # Se o usuário não cancelar a operação
        with open(caminho_arquivo, "w") as arquivo:
            arquivo.write(texto)
        msg_usuario.config(text=f"Mensagem salva com sucesso em '{caminho_arquivo}'!", fg="#4caf50")


# Configuração da interface gráfica
app = tk.Tk()
app.title("KeyCipher")
app.geometry("700x400")
app.configure(bg="#2b2b2b")  # Fundo da janela principal ( modo escuro, pra mim é mais agradável )


# Widgets
tk.Label(app, text="Mensagem:", bg="#2b2b2b", fg="#ffffff", font=("Helvetica", 10)).pack(pady=5)
entrada = tk.Entry(app, width=50, bg="#3c3f41", fg="#ffffff", insertbackground="#ffffff")
entrada.pack(pady=5)


tk.Label(app, text="Apenas letras do alfabeto sem acento ou caracteres especiais são aceitas", bg="#2b2b2b", fg="#ffcc00", font=("Helvetica", 8 )).pack(pady=2)


frame_botoes = tk.Frame(app, bg="#2b2b2b")  # Fundo do frame
frame_botoes.pack(pady=10)


btn_criptografar = tk.Button(frame_botoes, text="Criptografar", command=executar_criptografia, bg="#4caf50", fg="#ffffff", font=("Helvetica", 10))
btn_criptografar.grid(row=0, column=0, padx=10)


btn_descriptografar = tk.Button(frame_botoes, text="Descriptografar", command=executar_descriptografia, bg="#f44336", fg="#ffffff", font=("Helvetica", 10))
btn_descriptografar.grid(row=0, column=1, padx=10)


saida = tk.Text(app, width=50, height=5, bg="#3c3f41", fg="#ffffff", insertbackground="#ffffff", state="disabled")
saida.pack(pady=10)


btn_salvar = tk.Button(app, text="Salvar Mensagem", command=salvar_arquivo, bg="#2196f3", fg="#ffffff", font=("Helvetica", 10))
btn_salvar.pack(pady=10)


tk.Label(app, text="https://github.com/GabrielAlves7607 - GitHub", bg="#2b2b2b", fg="#ffcc00", font=("Helvetica", 8 )).pack(pady=2)
tk.Label(app, text="www.linkedin.com/in/joão-gabriel-alves-rocha-143651307 - Linkedin", bg="#2b2b2b", fg="#ffcc00", font=("Helvetica", 8 )).pack(pady=2)


msg_usuario = tk.Label(app, text="", bg="#2b2b2b", fg="#ffffff", font=("Helvetica", 10))
msg_usuario.pack(pady=5)


# Loop principal
app.mainloop()

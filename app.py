import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                shifted = ord('A') + (ord(char) - ord('A') + shift) % 26
            else:
                shifted = ord('a') + (ord(char) - ord('a') + shift) % 26
            result += chr(shifted)
        else:
            result += char
    return result

def encrypt():
    text = input_text.get("1.0",'end-1c')
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher(text, shift, "encrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", encrypted_text)

def decrypt():
    text = input_text.get("1.0",'end-1c')
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher(text, -shift, "decrypt")
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher")

input_label = tk.Label(root, text="Enter Text:")
input_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

input_text = tk.Text(root, height=5, width=40)
input_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

shift_label = tk.Label(root, text="Enter Shift:")
shift_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

shift_entry = tk.Entry(root)
shift_entry.grid(row=1, column=1, padx=5, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=2, padx=5, pady=5, sticky="ew")

output_label = tk.Label(root, text="Result:")
output_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

output_text = tk.Text(root, height=5, width=40)
output_text.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

root.mainloop()

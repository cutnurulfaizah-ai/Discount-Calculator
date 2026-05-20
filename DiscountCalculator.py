import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        price = float(entry_price.get())
        discount = float(entry_discount.get())

        final_price = price - (price * discount / 100)

        result_label.config(
            text=f"Final Price: Rp. {final_price:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Discount Calculator")
root.geometry("300x250")
label_price = tk.Label(root, text="Original Price:")
label_price.pack(pady=5)
entry_price = tk.Entry(root)
entry_price.pack(pady=5)
label_discount = tk.Label(root, text="Discount (%):")
label_discount.pack(pady=5)
entry_discount = tk.Entry(root)
entry_discount.pack(pady=5)
btn_calculate = tk.Button(
    root,
    text="Calculate",
    command=calculate_discount
)
btn_calculate.pack(pady=15)
result_label = tk.Label(
    root,
    text="Final Price: Rp. 0.00",
)
result_label.pack(pady=10)
root.mainloop()
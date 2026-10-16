import tkinter as tk
from tkinter import ttk

cua_so = tk.Tk()
cua_so.title("Vi du Combobox")
cua_so.geometry("350x200")

tk.Label(
    cua_so,
    text="Chon thanh pho:",
    font=("Arial", 12)
).pack(pady=10)

combobox_thanh_pho = ttk.Combobox(
    cua_so,
    values=["Ha Noi", "Da Nang", "TP.HCM", "Hue"],
    state="readonly"
)

combobox_thanh_pho.current(0)
combobox_thanh_pho.pack(pady=5)

def xem_thanh_pho():
    thanh_pho = combobox_thanh_pho.get()
    nhan_ket_qua.config(text=f"Ban chon: {thanh_pho}")

tk.Button(
    cua_so,
    text="Xac nhan",
    command=xem_thanh_pho
).pack(pady=10)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()
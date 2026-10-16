import tkinter as tk
from tkinter import messagebox

cua_so = tk.Tk()
cua_so.title("Vi du Listbox")
cua_so.geometry("300x300")

tk.Label(
    cua_so,
    text="Chon mon hoc:",
    font=("Arial", 12)
).pack(pady=10)

# Tao danh sach mon hoc
listbox_mon_hoc = tk.Listbox(
    cua_so,
    selectmode="single",
    height=5
)

for mon in ["Toan", "Ly", "Hoa", "Van", "Anh"]:
    listbox_mon_hoc.insert(tk.END, mon)

listbox_mon_hoc.pack(pady=10)

# Ham xem mon da chon
def xem_mon_da_chon():
    lua_chon = listbox_mon_hoc.curselection()

    if lua_chon:
        mon = listbox_mon_hoc.get(lua_chon[0])
        nhan_ket_qua.config(text=f"Mon da chon: {mon}")
    else:
        messagebox.showwarning(
            "Thong bao",
            "Vui long chon mot mon hoc!"
        )

tk.Button(
    cua_so,
    text="Xem mon da chon",
    command=xem_mon_da_chon
).pack(pady=5)

nhan_ket_qua = tk.Label(cua_so, text="")
nhan_ket_qua.pack()

cua_so.mainloop()
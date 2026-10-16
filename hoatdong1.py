import tkinter as tk

# Tao cua so
cua_so = tk.Tk()
cua_so.title("Vi du Checkbutton")
cua_so.geometry("300x250")

# Tieu de
tk.Label(
    cua_so,
    text="Chon so thich cua ban:",
    font=("Arial", 12)
).pack(pady=10)

# Bien dieu khien
bien_doc_sach = tk.BooleanVar()
bien_the_thao = tk.BooleanVar()
bien_am_nhac = tk.BooleanVar()

# Tao cac Checkbutton
tk.Checkbutton(
    cua_so,
    text="Doc sach",
    variable=bien_doc_sach
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so,
    text="The thao",
    variable=bien_the_thao
).pack(anchor="w", padx=30)

tk.Checkbutton(
    cua_so,
    text="Am nhac",
    variable=bien_am_nhac
).pack(anchor="w", padx=30)

# Ham xem lua chon
def xem_lua_chon():
    print("Doc sach:", bien_doc_sach.get())
    print("The thao:", bien_the_thao.get())
    print("Am nhac:", bien_am_nhac.get())

# Nut bam
tk.Button(
    cua_so,
    text="Xem lua chon",
    command=xem_lua_chon
).pack(pady=15)

# Chay giao dien
cua_so.mainloop()
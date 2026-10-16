import tkinter as tk
from tkinter import messagebox

# Tao cua so
cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("350x450")
cua_so.resizable(False, False)

# Bien luu bieu thuc
bieu_thuc = tk.StringVar()

# O hien thi bieu thuc va ket qua
o_hien_thi = tk.Entry(
    cua_so,
    textvariable=bieu_thuc,
    font=("Arial", 22),
    justify="right",
    state="readonly",
    readonlybackground="white"
)
o_hien_thi.grid(
    row=0,
    column=0,
    columnspan=4,
    padx=10,
    pady=15,
    ipady=12,
    sticky="nsew"
)

# Ham them ky tu vao bieu thuc
def them_ky_tu(ky_tu):
    bieu_thuc.set(bieu_thuc.get() + ky_tu)

# Ham xoa toan bo
def xoa_tat_ca():
    bieu_thuc.set("")

# Ham xoa mot ky tu
def xoa_mot_ky_tu():
    bieu_thuc.set(bieu_thuc.get()[:-1])

# Ham tinh ket qua
def tinh_ket_qua():
    bt = bieu_thuc.get().strip()

    if bt == "":
        messagebox.showwarning(
            "Thong bao",
            "Vui long nhap bieu thuc!"
        )
        return

    # Chi cho phep cac ky tu cua phep tinh co ban
    ky_tu_hop_le = "0123456789+-*/.() "

    if any(ky_tu not in ky_tu_hop_le for ky_tu in bt):
        messagebox.showerror(
            "Loi",
            "Bieu thuc chua ky tu khong hop le!"
        )
        return

    try:
        # Tinh bieu thuc
        ket_qua = eval(bt, {"__builtins__": {}}, {})

        # Khong hien thi .0 neu ket qua la so nguyen
        if isinstance(ket_qua, (int, float)):
            if isinstance(ket_qua, float) and ket_qua.is_integer():
                ket_qua = int(ket_qua)

        bieu_thuc.set(str(ket_qua))

    except ZeroDivisionError:
        messagebox.showerror(
            "Loi",
            "Khong the chia cho 0!"
        )

    except (SyntaxError, TypeError, ValueError, OverflowError):
        messagebox.showerror(
            "Loi",
            "Bieu thuc khong hop le!"
        )

# Cac phim tren ban phim
cac_phim = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Tao cac nut bam
for ten_phim, hang, cot in cac_phim:
    if ten_phim == "=":
        nut = tk.Button(
            cua_so,
            text=ten_phim,
            font=("Arial", 16),
            command=tinh_ket_qua
        )
    else:
        nut = tk.Button(
            cua_so,
            text=ten_phim,
            font=("Arial", 16),
            command=lambda ky_tu=ten_phim: them_ky_tu(ky_tu)
        )

    nut.grid(
        row=hang,
        column=cot,
        padx=4,
        pady=4,
        sticky="nsew",
        ipadx=5,
        ipady=10
    )

# Nut xoa
tk.Button(
    cua_so,
    text="C",
    font=("Arial", 14),
    command=xoa_tat_ca
).grid(
    row=5,
    column=0,
    columnspan=2,
    padx=4,
    pady=4,
    sticky="nsew"
)

# Nut xoa mot ky tu
tk.Button(
    cua_so,
    text="⌫",
    font=("Arial", 14),command=xoa_mot_ky_tu
).grid(
    row=5,
    column=2,
    columnspan=2,
    padx=4,
    pady=4,
    sticky="nsew"
)

# Tu dong gian deu cac hang va cot
for cot in range(4):
    cua_so.grid_columnconfigure(cot, weight=1)

for hang in range(6):
    cua_so.grid_rowconfigure(hang, weight=1)

# Chay chuong trinh
cua_so.mainloop()
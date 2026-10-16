import tkinter as tk
from tkinter import messagebox


# Mỗi công việc gồm nội dung và trạng thái hoàn thành
danh_sach_cong_viec = []


def lam_moi_listbox():
    listbox_cong_viec.delete(0, tk.END)

    for noi_dung, da_hoan_thanh in danh_sach_cong_viec:
        if da_hoan_thanh:
            tien_to = "[Da xong] "
        else:
            tien_to = "[Chua xong] "

        listbox_cong_viec.insert(
            tk.END,
            tien_to + noi_dung
        )


def them_cong_viec():
    noi_dung = bien_cong_viec_moi.get().strip()

    if noi_dung == "":
        messagebox.showerror(
            "Lỗi",
            "Vui lòng nhập nội dung công việc trước khi thêm!"
        )
        return

    danh_sach_cong_viec.append((noi_dung, False))

    bien_cong_viec_moi.set("")
    lam_moi_listbox()


def xoa_cong_viec():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror(
            "Lỗi",
            "Vui lòng chọn một công việc trong danh sách để xóa."
        )
        return

    vi_tri = lua_chon[0]
    danh_sach_cong_viec.pop(vi_tri)

    lam_moi_listbox()


def danh_dau_hoan_thanh():
    lua_chon = listbox_cong_viec.curselection()

    if not lua_chon:
        messagebox.showerror(
            "Lỗi",
            "Vui lòng chọn một công việc để đánh dấu hoàn thành."
        )
        return

    vi_tri = lua_chon[0]
    noi_dung, da_hoan_thanh = danh_sach_cong_viec[vi_tri]

    # Đảo trạng thái: chưa xong -> xong, xong -> chưa xong
    danh_sach_cong_viec[vi_tri] = (
        noi_dung,
        not da_hoan_thanh
    )

    lam_moi_listbox()


# Tạo cửa sổ
cua_so = tk.Tk()
cua_so.title("Ứng dụng Ghi chú công việc")
cua_so.geometry("500x430")
cua_so.resizable(False, False)

bien_cong_viec_moi = tk.StringVar()

# Tiêu đề
tk.Label(
    cua_so,
    text="TO-DO LIST",
    font=("Arial", 18, "bold")
).grid(
    row=0, column=0, columnspan=3, pady=15
)

# Ô nhập công việc
entry_cong_viec = tk.Entry(
    cua_so,
    textvariable=bien_cong_viec_moi,
    width=35,
    font=("Arial", 11)
)
entry_cong_viec.grid(
    row=1, column=0, columnspan=2,
    padx=10, pady=5
)

# Nút thêm
tk.Button(
    cua_so,
    text="Thêm",
    width=10,
    command=them_cong_viec
).grid(row=1, column=2, padx=5, pady=5)

# Danh sách công việc
listbox_cong_viec = tk.Listbox(
    cua_so,
    width=55,
    height=13,
    font=("Arial", 10),
    selectmode="single"
)
listbox_cong_viec.grid(
    row=2, column=0, columnspan=3,
    padx=10, pady=10
)

# Nút đánh dấu hoàn thành
tk.Button(
    cua_so,
    text="Đánh dấu hoàn thành",
    command=danh_dau_hoan_thanh
).grid(row=3, column=0, padx=5, pady=10)

# Nút xóa
tk.Button(
    cua_so,
    text="Xóa công việc",
    command=xoa_cong_viec
).grid(row=3, column=1, padx=5, pady=10)

# Nút thoát
tk.Button(
    cua_so,
    text="Thoát",
    command=cua_so.destroy).grid(row=3, column=2, padx=5, pady=10)

# Cho phép nhấn Enter để thêm công việc
entry_cong_viec.bind(
    "<Return>",
    lambda event: them_cong_viec()
)

cua_so.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import data_access

theme_mode = "dark"  # or "light"

def apply_theme():
    if theme_mode == "dark":
        root.configure(bg="black")
        btn_frame.configure(bg="black")
        style.configure("Treeview",
            background="black",
            foreground="blue",
            fieldbackground="black",
            font=('Arial', 10)
        )
        style.configure("Treeview.Heading",
            background="gray20",
            foreground="white"
        )
    else:
        root.configure(bg="white")
        btn_frame.configure(bg="white")
        style.configure("Treeview",
            background="white",
            foreground="black",
            fieldbackground="white",
            font=('Arial', 10)
        )
        style.configure("Treeview.Heading",
            background="lightgray",
            foreground="black"
        )

    for btn in btn_frame.winfo_children():
        btn.configure(
            bg="gray20" if theme_mode == "dark" else "lightgray",
            fg="white" if theme_mode == "dark" else "black",
            activebackground="gray30" if theme_mode == "dark" else "gray70",
            activeforeground="cyan" if theme_mode == "dark" else "black"
        )

def toggle_theme():
    global theme_mode
    theme_mode = "light" if theme_mode == "dark" else "dark"
    apply_theme()

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for vehicle in data_access.fetch_all_vehicles():
        tree.insert("", "end", values=vehicle)

def add_vehicle_popup():
    def submit():
        try:
            vehicle = (
                entry_type.get(),
                entry_make.get(),
                entry_model.get(),
                int(entry_hp.get()),
                int(entry_seats.get()),
                int(entry_max_kmh.get()),
                int(entry_year.get()),
                entry_plate.get()
            )
            data_access.insert_vehicle(*vehicle)
            messagebox.showinfo("Success", "Vehicle added.")
            popup.destroy()
            refresh_table()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    popup = tk.Toplevel(root)
    popup.title("Add Vehicle")
    popup.configure(bg="black" if theme_mode == "dark" else "white")

    fields = ["Type", "Make", "Model", "HP", "Seats", "Max km/h", "Year", "License Plate"]
    entries = []

    for i, field in enumerate(fields):
        tk.Label(popup, text=field, bg="black" if theme_mode == "dark" else "white",
                 fg="white" if theme_mode == "dark" else "black").grid(row=i, column=0, padx=5, pady=5)
        entry = tk.Entry(popup, bg="gray20" if theme_mode == "dark" else "white",
                         fg="white" if theme_mode == "dark" else "black",
                         insertbackground="white" if theme_mode == "dark" else "black")
        entry.grid(row=i, column=1, padx=5, pady=5)
        entries.append(entry)

    (entry_type, entry_make, entry_model, entry_hp,
     entry_seats, entry_max_kmh, entry_year, entry_plate) = entries

    tk.Button(popup, text="Submit", command=submit,
              bg="gray30" if theme_mode == "dark" else "lightgray",
              fg="white" if theme_mode == "dark" else "black",
              activebackground="gray40" if theme_mode == "dark" else "gray70").grid(
        row=len(fields), column=0, columnspan=2, pady=10)

def delete_selected():
    selected = tree.focus()
    if not selected:
        messagebox.showwarning("No selection", "Please select a vehicle to delete.")
        return

    values = tree.item(selected, 'values')
    license_plate = values[-1]
    confirm = messagebox.askyesno("Confirm Delete", f"Delete vehicle {license_plate}?")
    if confirm:
        data_access.delete_vehicle_by_plate(license_plate)
        refresh_table()

# --- Main Window ---
root = tk.Tk()
root.title("Car Inventory Manager")
root.geometry("900x400")

style = ttk.Style()
style.theme_use("default")

columns = ("ID", "Type", "Make", "Model", "HP", "Seats", "Max km/h", "Year", "Plate")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", width=100)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

def make_button(text, command):
    return tk.Button(
        btn_frame, text=text, command=command, width=20
    )

make_button("Add Vehicle", add_vehicle_popup).pack(side="left", padx=5)
make_button("Delete Selected", delete_selected).pack(side="left", padx=5)
make_button("Refresh List", refresh_table).pack(side="left", padx=5)
make_button("Toggle Theme", toggle_theme).pack(side="left", padx=5)

apply_theme()
refresh_table()
root.mainloop()

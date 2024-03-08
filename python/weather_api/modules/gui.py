import tkinter
from tkinter import ttk
from tkinter import font
from modules.get import get_data
from modules.convert import convert_data


class GUI:
    def __init__(self):
        self.form = tkinter.Tk()
        self.form.title("Weather display")
        self.form.geometry("600x400+500+200")
        self.form.config(background="#0b0c10")
        self.form.resizable(False, False)
        self.font = font.Font(family="Times New Roman", size=20)
        self.style = ttk.Style()
        self.style.configure("TButton", background="#0b0c10")
        self.table = ttk.Treeview()
        self.error = ttk.Label(
            self.form,
            font=self.font,
            background="#0b0c10",
            foreground="#ff0f50",
            padding=10,
            width=19,
        )
        self.error.place(x=15, y=100)
        self.label = ttk.Label(
            self.form,
            font=self.font,
            background="#0b0c10",
            foreground="#ffffff",
            text="Enter city name:",
            justify="left",
        )
        self.entry = ttk.Entry(self.form, font=self.font, width=20)
        self.button = ttk.Button(
            self.form,
            text="Send",
            command=self.handle_click,
            padding=6,
            takefocus=False,
            style="TButton",
        )

        self.label.pack(anchor="w", padx=15, pady=10)
        self.entry.place(x=15, y=50)
        self.button.place(x=350, y=50)

    def run(self):
        self.form.mainloop()

    def handle_click(self):
        self.city = self.entry.get()
        self.data = get_data(self.city)
        self.data = convert_data(self.data)
        if "city" in self.data:
            self.table = ttk.Treeview(
                self.form, show="headings", columns=("key", "value")
            )
            self.table.heading("key", text="Key")
            self.table.column("key", width=150)
            self.table.heading("value", text="Value")
            self.table.column("value", width=150)
            self.table.tag_configure("heading", font="Times")
            self.table.place(x=15, y=100)

            for key, val in self.data.items():
                self.table.insert("", "end", values=(key, val), tags="heading")
            self.image_file = f"./pngs/{self.data['state']}.png"
            self.image = tkinter.PhotoImage(file=self.image_file)
            self.image_label = ttk.Label(
                self.form, background="#0b0c10", image=self.image
            )
            self.image_label.place(x=350, y=100)
        else:
            if self.table.winfo_exists():
                self.table.destroy()
                self.image_label.destroy()
            self.error["text"] = self.data["message"]

from tkinter import filedialog
import csv
import customtkinter
from CTkMessagebox import CTkMessagebox

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("CSV Combine")
        self.geometry(f"{940}x{340}")
        self.resizable(False, False)
        self.iconbitmap("./theme/icon.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_rowconfigure((2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Import CSVs",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Add CSV 1",
                                                        command=self.sidebar_button_event1)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add CSV 2",
                                                        command=self.sidebar_button_event2)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Insert Common Row Name")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(10, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, text="Combine CSVs", fg_color="transparent",
                                                     border_width=2, text_color=("gray10", "#DCE4EE"),
                                                     command=self.combine_csvs)
        self.main_button_1.grid(row=3, column=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox1 = customtkinter.CTkTextbox(self, width=50, wrap="none")
        self.textbox1.grid(row=1, column=1, padx=(20, 10), pady=(0, 0), sticky="nsew")
        self.textbox2 = customtkinter.CTkTextbox(self, width=50, wrap="none")
        self.textbox2.grid(row=1, column=2, padx=(10, 20), pady=(0, 0), sticky="nsew")
        self.appearance_mode_label1 = customtkinter.CTkLabel(self, text="CSV 1")
        self.appearance_mode_label1.grid(row=0, column=1, padx=(20, 10), sticky="nsew")
        self.appearance_mode_label2 = customtkinter.CTkLabel(self, text="CSV 2")
        self.appearance_mode_label2.grid(row=0, column=2, padx=(10, 20), sticky="nsew")

    def sidebar_button_event1(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textbox1.delete("0.0", customtkinter.END)  # Clear existing content
                self.textbox1.insert(customtkinter.END, content)

    def sidebar_button_event2(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.textbox2.delete("0.0", customtkinter.END)  # Clear existing content
                self.textbox2.insert(customtkinter.END, content)

    def combine_csvs(self):
        common_row_name = self.entry.get()
        if not common_row_name:
            CTkMessagebox(message="Please enter in Row name.", title="Error", icon='cancel')
            return

        content1 = self.textbox1.get("0.0", customtkinter.END)
        content2 = self.textbox2.get("0.0", customtkinter.END)

        if not content1 or not content2:
            CTkMessagebox(message="Please add both CSVs", title="Error", icon='cancel')
            return

        # Parse CSV content as dictionaries
        csv_data1 = csv.DictReader(content1.splitlines())
        csv_data2 = csv.DictReader(content2.splitlines())

        # Combine CSV data
        combined_data = []
        header1 = csv_data1.fieldnames
        header2 = csv_data2.fieldnames

        # Remove duplicate columns
        combined_header = header1 + [column for column in header2 if column not in header1]
        combined_data.append(combined_header)

        for row1 in csv_data1:
            csv_data2 = csv.DictReader(content2.splitlines())  # Reset csv_data2 for each row in csv_data1
            for row2 in csv_data2:
                if row1[common_row_name] == row2[common_row_name]:
                    combined_row = [row1[column] for column in header1] + [row2[column] for column in header2 if
                                                                           column not in header1]
                    combined_data.append(combined_row)

        # Save combined data to a new CSV file
        save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if save_path:
            with open(save_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(combined_data)

    def mainloop(self):
        customtkinter.CTk.mainloop(self)


if __name__ == "__main__":
    app = App()
    app.mainloop()

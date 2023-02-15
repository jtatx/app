import os
import csv

import tkinter as tk
from PIL import Image, UnidentifiedImageError
from tkinter import filedialog, messagebox


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.folder_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.select_folder_button = tk.Button(
            self.master, text="Select Folder", command=self.select_folder
        )
        self.select_folder_button.pack()

        self.folder_path_label = tk.Label(
            self.master, textvariable=self.folder_path, wraplength=400
        )
        self.folder_path_label.pack()

        self.select_output_button = tk.Button(
            self.master, text="Select Output Location", command=self.select_output
        )
        self.select_output_button.pack()

        self.output_path_label = tk.Label(
            self.master, textvariable=self.output_path, wraplength=400
        )
        self.output_path_label.pack()

        self.start_button = tk.Button(self.master, text="Start", command=self.start)
        self.start_button.pack()

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)

    def select_output(self):
        output_selected = filedialog.asksaveasfilename(
            defaultextension=".csv", initialfile="orientations.csv"
        )
        if output_selected:
            self.output_path.set(output_selected)

    def get_orientation(self, image: Image.Image):
        aspect_ratio = image.width / image.height

        if aspect_ratio > 1.0:
            return "Landscape"
        elif aspect_ratio < 1.0:
            return "Portrait"
        else:
            return "Square"

    def start(self):
        folder_path = self.folder_path.get()
        if not folder_path:
            messagebox.showerror("Error", "Please select a folder.")
            return

        output_path = self.output_path.get()
        if not output_path:
            messagebox.showerror("Error", "Please select an output location.")
            return

        images = []
        for file in os.listdir(folder_path):
            if file.lower().endswith((".jpg", ".jpeg", ".png")):
                file_path = os.path.join(folder_path, file)
                try:
                    with Image.open(file_path) as image:
                        orientation = self.get_orientation(image)
                        images.append((file, orientation))
                except (AttributeError, UnidentifiedImageError):
                    pass

        if not images:
            messagebox.showwarning("Warning", "No images found in the folder.")
            return

        with open(output_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["File", "Orientation"])
            writer.writerows(images)

        messagebox.showinfo(
            "Info",
            f"{len(images)} images found. Orientations exported to {output_path}.",
        )


def main():
    root = tk.Tk()
    root.title("Image Orientation Finder")
    root.geometry("500x250")
    app = App(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
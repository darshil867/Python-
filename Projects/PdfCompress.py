import os
import pikepdf
import customtkinter as ctk
from tkinter import filedialog, messagebox


def compress_pdf(input_path, output_path):

    try:

        with pikepdf.Pdf.open(input_path) as pdf:

            pdf.save(output_path, compress_streams=True)

        messagebox.showinfo("Success", f"PDF successfully compressed and saved to:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during compression:\n{e}")


def select_pdf():

    file_path = filedialog.askopenfilename(
        title="Select a PDF File",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if file_path:
        global selected_pdf
        selected_pdf = file_path
        label_selected_file.configure(text=f"Selected: {os.path.basename(file_path)}")
    else:
        label_selected_file.configure(text="No file selected")


def save_compressed_pdf():

    if not selected_pdf:
        messagebox.showwarning("No File", "Please select a PDF file first.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Compressed PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if output_file:
        compress_pdf(selected_pdf, output_file)

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("PDF Compressor")
app.geometry("500x300")

selected_pdf = None


label_title = ctk.CTkLabel(app, text="PDF Compressor", font=("Arial", 20))
label_title.pack(pady=20)

btn_select_pdf = ctk.CTkButton(app, text="Select PDF", command=select_pdf, width=200)
btn_select_pdf.pack(pady=10)

label_selected_file = ctk.CTkLabel(app, text="No file selected", font=("Arial", 12))
label_selected_file.pack(pady=5)

btn_compress_pdf = ctk.CTkButton(app, text="Compress PDF", command=save_compressed_pdf, width=200)
btn_compress_pdf.pack(pady=20)

app.mainloop()

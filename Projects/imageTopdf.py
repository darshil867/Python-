import os
from PIL import Image
from PyPDF2 import PdfWriter
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Global variable to store selected image paths
selected_images = []


def convert_images_to_pdf(image_paths, output_pdf_path):
    """
    Convert multiple images to a single PDF without quality loss.

    Args:
        image_paths (list): List of paths to input image files.
        output_pdf_path (str): Path to the output PDF file.
    """
    try:
        pdf_writer = PdfWriter()

        for image_path in image_paths:
            image = Image.open(image_path)
            if image.mode != 'RGB':
                image = image.convert('RGB')
            temp_pdf_path = f"{os.path.splitext(image_path)[0]}.temp.pdf"
            # Save high-resolution image directly into a temporary PDF
            image.save(temp_pdf_path, format="PDF", resolution=300.0)
            with open(temp_pdf_path, "rb") as temp_pdf_file:
                pdf_writer.append(temp_pdf_file)
            os.remove(temp_pdf_path)

        with open(output_pdf_path, "wb") as output_file:
            pdf_writer.write(output_file)

        messagebox.showinfo("Success", f"Images successfully converted to PDF: {output_pdf_path}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def select_images():
    """
    Open a file dialog to select images.
    """
    global selected_images
    file_paths = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )
    if file_paths:
        selected_images = list(file_paths)  # Update the global variable
        label_selected_files.configure(
            text=f"{len(selected_images)} file(s) selected"  # Update the label text
        )
    else:
        label_selected_files.configure(text="No files selected")


def save_pdf():
    """
    Save the PDF after converting images.
    """
    if not selected_images:
        messagebox.showwarning("No Files", "Please select image files first.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save PDF As",
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if output_file:
        convert_images_to_pdf(selected_images, output_file)


# CustomTkinter UI Initialization
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("High-Quality Image to PDF Converter")
app.geometry("500x300")

# Widgets
label_title = ctk.CTkLabel(
    app, text="High-Quality Image to PDF Converter", font=("Arial", 20)
)
label_title.pack(pady=20)

btn_select_images = ctk.CTkButton(
    app, text="Select Images", command=select_images, width=200
)
btn_select_images.pack(pady=10)

label_selected_files = ctk.CTkLabel(
    app, text="No files selected", font=("Arial", 12)
)
label_selected_files.pack(pady=5)

btn_save_pdf = ctk.CTkButton(
    app, text="Convert to PDF", command=save_pdf, width=200
)
btn_save_pdf.pack(pady=20)

# Run the application
app.mainloop()

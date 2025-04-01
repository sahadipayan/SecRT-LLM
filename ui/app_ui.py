import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from detection.detection_controller import start_detection
from utils.file_utils import write_temp_path

def launch_app():
    root = tk.Tk()
    root.title("SecRT-LLM: Vulnerability Detection Framework")
    root.geometry("1080x800")
    root.configure(bg="#204abe")

    canvas = tk.Canvas(root, bg="#204abe")
    canvas.pack(fill=tk.BOTH, expand=1)

    tk.Label(canvas,
        text="SecRT-LLM: HW Security Bug Detection Using Large Language Model",
        font=("Raleway", 24),
        fg="white",
        bg="#204abe"
    ).grid(column=0, row=0, padx=20, pady=10, sticky="N")

    logo_image = Image.open("assets/universityofflorida3.jpg")
    logo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(canvas, image=logo, bg="#204abe")
    logo_label.image = logo
    logo_label.grid(column=0, row=1, pady=10, sticky="N")

    tk.Button(canvas,
        text="Vulnerability Detection",
        command=lambda: open_detection_window(root),
        font=("Raleway", 20, 'bold'),
        bg="#204abe",
        fg="white",
        height=3,
        width=24
    ).grid(column=0, pady=20, row=3, sticky="N")

    tk.Label(canvas,
        text="Developed by\nDipayan Saha\n Sujan Kumer Saha\nMark Tehranipoor\nFarimah Farahmandi",
        font=("Raleway", 16, "italic"),
        fg="white",
        bg="#204abe",
        justify="center"
    ).grid(column=0, row=6, pady=(50, 10), sticky="S")

    root.mainloop()

def open_detection_window(root):
    protected_state = tk.StringVar()
    report_buttons = []
    open_report_button = None
    window = tk.Toplevel(root)
    window.title("Vulnerability Detection")
    window.geometry("1000x600")
    canvas = tk.Canvas(window, bg="#204abe")
    canvas.pack(fill=tk.BOTH, expand=1)

    uploaded_file_label = tk.StringVar()
    status_label = tk.Label(canvas, font=("Raleway", 12, "bold"), bg="#204abe", fg="white")

    tk.Label(canvas, text="Step 1: Upload your design", font=("Raleway", 12, "bold"), bg="#204abe", fg="white").pack(pady=5)

    def upload_file():
        from tkinter.filedialog import askopenfile
        file = askopenfile(parent=window, mode='rb', title="Choose a Verilog File", filetypes=[("Verilog File", "*.v"), ("All Files", "*.*")])
        if file:
            uploaded_file_label.set(file.name)
            write_temp_path(file.name)

    tk.Button(canvas, text="Upload Input Design", font=("Raleway", 12, "bold"), bg="#204abe", fg="white", command=upload_file).pack(pady=5)
    tk.Label(canvas, textvariable=uploaded_file_label, font=("Raleway", 12, "bold"), bg="#204abe", fg="white").pack(pady=5)

    tk.Label(canvas, text="Step 2: Choose a vulnerability", font=("Raleway", 12, "bold"), bg="#204abe", fg="white").pack(pady=5)
    dropdown1 = ttk.Combobox(canvas, values=[
        "V1 (Hamming Distance)",
        "V2 (Static Deadlock)",
        "V4 (Dead State)",
        "V5 (Unreachable State Detection)",
        "V7 (Duplicate Encoding)"
    ], font=("Raleway", 12, "bold"))
    dropdown1.set("Select the vulnerability")
    dropdown1.pack(pady=5)

    tk.Label(canvas, text="Step 3: Select LLM", font=("Raleway", 12, "bold"), bg="#204abe", fg="white").pack(pady=5)
    dropdown2 = ttk.Combobox(canvas, values=["gpt-3.5-turbo", "gpt-4", "gpt-4o"], font=("Raleway", 12, "bold"))
    dropdown2.set("Select LLM")
    dropdown2.pack(pady=5)

    tk.Label(canvas, text="Step 4: (For V1) Enter Protected State", font=("Raleway", 12, "bold"), bg="#204abe", fg="white").pack(pady=5)
    tk.Entry(canvas, textvariable=protected_state, font=("Raleway", 12, "bold"), width=30).pack(pady=5)

    def run_detection():
        vuln = dropdown1.get()
        llm = dropdown2.get()
        if uploaded_file_label.get():
            status_label.config(text="Processing... Please wait.", fg="white")
            start_detection(vuln, llm, status_label, canvas, protected_state.get())
            for widget in canvas.winfo_children():
                if isinstance(widget, tk.Button) and widget.cget('text') == 'Open Full Report':
                    report_buttons.append(widget)

        else:
            status_label.config(text="Please upload a file first.", fg="red")

    tk.Button(canvas, text="Start Detection", font=("Raleway", 12, "bold"), bg="#204abe", fg="white", command=run_detection).pack(pady=10)
    status_label.pack(pady=10)

    def reset_inputs():
        uploaded_file_label.set("")
        dropdown1.set("Select the vulnerability")
        dropdown2.set("Select LLM")
        protected_state.set("")
        status_label.config(text="")
        
        # Remove all report buttons
        for btn in report_buttons:
            btn.destroy()
        report_buttons.clear()

    tk.Button(canvas, text="Refresh", font=("Raleway", 12, "bold"), bg="orange", fg="white", command=reset_inputs).pack(pady=5)

from detection.prompting_controller import handle_prompting_detection
from utils.constants import REPORT_FILE
import tkinter as tk
import subprocess as sp
import time

def start_detection(vulnerability, llm, status_label, canvas, protected_state=None):
    start = time.time()

    if vulnerability == "V1 (Hamming Distance)":
        result = handle_prompting_detection(vulnerability, llm, protected_state)
    else:
        result = handle_prompting_detection(vulnerability, llm)

    with open(REPORT_FILE, "w") as f:
        f.write(result)

    status_label.config(text=f"Detection completed in {time.time() - start:.2f}s. Report is ready.", fg="white")

    tk.Button(canvas, text="Open Full Report", font=("Raleway", 12, "bold"), bg="#204abe", fg="white", command=lambda: sp.Popen(["notepad.exe", REPORT_FILE])).pack(pady=10)

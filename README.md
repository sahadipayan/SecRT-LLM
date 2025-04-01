# SecRT-LLM
Hardware Vulnerability Detection Framework Using Large Language Model

SecRT-LLM is a framework designed to detect hardware security vulnerabilities in Verilog designs using Large Language Models (LLMs). It allows users to upload their design files, select specific vulnerabilities, and use state-of-the-art LLMs like GPT-4 to analyze and report potential issues.

---

## Features

- LLM-powered detection using GPT-3.5, GPT-4, and GPT-4o
- Upload and analyze Verilog HDL designs
- Detects a variety of vulnerabilities including:
  - Hamming Distance Violations (V1)
  - Static Deadlock Detection (V2)
  - Dead State Analysis (V4)
  - Unreachable State Detection (V5)
  - Duplicate Encoding (V7)
- Simple and intuitive GUI built with Tkinter
- Generates detailed reports after each detection

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/sahadipayan/SecRT-LLM.git
cd SecRT-LLM
```

### 2. Create a Virtual Environment (optional but recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add OpenAI API Key 
edit api_key.txt by adding OpenAI API Key

### 5. Run the Application
```bash
python app.py
```
The GUI will launch, and you can start uploading and analyzing your designs!

### Project Structure
```bash
SecRT-LLM/
├── app.py                     # Main application launcher
├── assets/                   # Images and visual assets
│   └── universityofflorida3.jpg
├── detection/                # Core detection logic
│   └── detection_controller.py
├── utils/                    # Utility functions
│   └── file_utils.py
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

### Developed by
Dipayan Saha (dsaha@ufl.edu), University of Florida
Sujan Kumar Saha, University of Florida
Mark Tehranipoor, University of Florida
Farimah Farahmandi, University of Florida

###  Citation
If you use this tool or any part of the framework in your research, please cite our HOST 2024 paper:

```bibtex
@inproceedings{saha2024empowering,
  title={Empowering hardware security with llm: The development of a vulnerable hardware database},
  author={Saha, Dipayan and Yahyaei, Katayoon and Saha, Sujan Kumar and Tehranipoor, Mark and Farahmandi, Farimah},
  booktitle={2024 IEEE International Symposium on Hardware Oriented Security and Trust (HOST)},
  pages={233--243},
  year={2024},
  organization={IEEE}
}
```
For citation in publications, please use the BibTeX entry above. We appreciate your support!



<div align="center">

<img src="https://img.icons8.com/fluency/96/000000/calculator.png" width="70" alt="Calculator Icon"/>

# Calci

### A minimal calculator web app built with Python and Streamlit

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-informational?style=for-the-badge&logo=open-source-initiative&logoColor=white)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-abhayraj81-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/abhayraj81)

</div>

---

## Overview

Calci is a lightweight calculator built with Python functions and wrapped in a clean [Streamlit](https://streamlit.io/) interface. It takes two numbers, lets you pick an operation, and returns the result instantly in the browser — no command line required.

## Features

| <img src="https://img.icons8.com/fluency/48/plus-math.png" width="22"/> Addition | <img src="https://img.icons8.com/fluency/48/minus-math.png" width="22"/> Subtraction | <img src="https://img.icons8.com/fluency/48/multiply.png" width="22"/> Multiplication | <img src="https://img.icons8.com/fluency/48/divide.png" width="22"/> Division | <img src="https://img.icons8.com/fluency/48/statistics.png" width="22"/> Average |
|:---:|:---:|:---:|:---:|:---:|
| `a + b` | `a - b` | `a × b` | `a / b` | `(a + b) / 2` |

- Clean, single-page UI with number inputs and a radio-button operation selector
- Handles divide-by-zero gracefully with an inline error message instead of crashing
- Instant results displayed with Streamlit's success banner

## Tech Stack

<img src="https://img.icons8.com/color/48/python.png" width="28"/> &nbsp;
<img src="https://img.icons8.com/color/48/streamlit.png" width="28"/> &nbsp;

- **Language:** Python 3
- **Framework:** Streamlit

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip

### Installation

```bash
git clone https://github.com/abhayraj81/Calci.git
cd Calci
pip install streamlit
```

### Run the App

```bash
streamlit run Calci.py
```

The app will open automatically in your default browser at `http://localhost:8501`.

## Project Structure

```
Calci/
└── Calci.py     # Core logic + Streamlit UI
```

## How It Works

Each arithmetic operation is implemented as an independent Python function (`add`, `sub`, `mul`, `div`, `avg`). The Streamlit UI collects two numbers and an operation choice from the user, then calls the corresponding function and displays the result.

## Author

<img src="https://img.icons8.com/fluency/48/user.png" width="20"/> **Abhay Raj**
[![GitHub](https://img.shields.io/badge/GitHub-abhayraj81-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/abhayraj81)

## License

This project is licensed under the MIT License.

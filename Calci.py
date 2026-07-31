import streamlit as st

# ---- Functions for all operations ----
def add(a, b):
    return a + b

def sub(a, b):
    if a > b:
        return a - b
    else:
        return -(b - a)

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def avg(a, b):
    return (a + b) / 2


# ---- Streamlit UI ----
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

st.title("🧮 Simple Calculator")
st.write("Select an operation and enter two numbers.")

col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Enter First Number", value=0.0, step=1.0)
with col2:
    b = st.number_input("Enter Second Number", value=0.0, step=1.0)

operation = st.radio(
    "Select Operation",
    ["Addition", "Subtraction", "Multiplication", "Division", "Average"],
    horizontal=True,
)

if st.button("Calculate", use_container_width=True):
    if operation == "Addition":
        result = add(a, b)
        st.success(f"{a} + {b} = {result}")
    elif operation == "Subtraction":
        result = sub(a, b)
        st.success(f"{a} - {b} = {result}")
    elif operation == "Multiplication":
        result = mul(a, b)
        st.success(f"{a} × {b} = {result}")
    elif operation == "Division":
        result = div(a, b)
        st.success(f"{a} / {b} = {result}")
    elif operation == "Average":
        result = avg(a, b)
        st.success(f"Average of {a} and {b} = {result}")

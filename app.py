import streamlit as st
import math

# Define calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def logarithm(x, base):
    return math.log(x, base)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Streamlit app
def scientific_calculator_app():
    st.title("Scientific Calculator")
   st.image("calculator.jpg", caption="Scientific Calculator", use_column_width=True)

    # Input for first number
    num1 = st.number_input("Enter first number", value=0.0)

    # Operation selection
    operation = st.selectbox("Select operation", 
        ["Add", "Subtract", "Multiply", "Divide", 
         "Square Root", "Power", "Logarithm", 
         "Sine", "Cosine", "Tangent"])

    # Button to calculate the result
    if operation in ["Add", "Subtract", "Multiply", "Divide", "Power", "Logarithm"]:
        num2 = st.number_input("Enter second number", value=0.0)

        if st.button("Calculate"):
            if operation == "Add":
                result = add(num1, num2)
            elif operation == "Subtract":
                result = subtract(num1, num2)
            elif operation == "Multiply":
                result = multiply(num1, num2)
            elif operation == "Divide":
                result = divide(num1, num2)
            elif operation == "Power":
                result = power(num1, num2)
            elif operation == "Logarithm":
                if num1 <= 0 or num2 <= 1:
                    result = "Error! Logarithm base must be greater than 1 and x must be positive."
                else:
                    result = logarithm(num1, num2)

    elif operation in ["Square Root", "Sine", "Cosine", "Tangent"]:
        if st.button("Calculate"):
            if operation == "Square Root":
                result = square_root(num1)
            elif operation == "Sine":
                result = sin(num1)
            elif operation == "Cosine":
                result = cos(num1)
            elif operation == "Tangent":
                result = tan(num1)

    # Display the result
    if 'result' in locals():
        st.success(f"The result is: {result}")

# Run the app
if __name__ == "__main__":
    scientific_calculator_app()

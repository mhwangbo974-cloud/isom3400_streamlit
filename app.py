import streamlit as st
import math


def calculate_basic_op(operation: str, num1: float, num2: float):
    if operation == "Add":
        return num1 + num2
    elif operation == "Subtract":
        return num1 - num2
    elif operation == "Multiply":
        return num1 * num2
    elif operation == "Divide":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == "sin()":
        return math.sin(num1)
    return None


def calculate_log_op(operation: str, num1: float):
    if num1 <= 0:
        return "Error: Logarithm input must be greater than 0"
    if operation == "log10()":
        return math.log10(num1)
    elif operation == "ln()":
        return math.log(num1)
    return None


def main():
    st.title("Basic Web Calculator")

    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)

    operations = ["Add", "Subtract", "Multiply", "Divide", "sin()", "log10()", "ln()"]
    operation = st.selectbox("Choose operation", operations)

    if operation in ("sin()", "log10()", "ln()"):
        st.caption("Uses the first number as the input.")

    if st.button("Calculate"):
        if operation in ("log10()", "ln()"):
            result = calculate_log_op(operation, num1)
        else:
            result = calculate_basic_op(operation, num1, num2)

        if isinstance(result, str) and result.startswith("Error:"):
            st.error(result)
        else:
            st.success(f"Result: {result}")


if __name__ == "__main__":
    main()

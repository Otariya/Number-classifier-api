from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

# Default number to use if no number is provided
DEFAULT_NUMBER = 42  

@app.get("/api/classify-number")
def classify_number(number: Optional[str] = Query(default=None, description="The number to classify")):
    print(f"Received number: {number}")  # Debugging: Print the received number
    
    # Handle missing parameter or empty string by using the default number
    if number is None or number == "":
        number = str(DEFAULT_NUMBER)  # Convert the default number to a string for consistency
        print(f"Using default number: {number}")  # Debugging: Print the default number
    
    # Validate input (must be a whole number, reject floats)
    try:
        if "." in number:
            raise ValueError("Invalid input: floating-point numbers are not allowed")
        num = int(number)
        print(f"Parsed number: {num}")  # Debugging: Print the parsed number
    except ValueError as e:
        print(f"Validation error: {e}")  # Debugging: Print validation error
        return JSONResponse(
            status_code=400,  # Use 400 for client errors
            content={"number": number, "error": True, "message": str(e)}
        )

    # Rest of the classification logic
    properties = ["even" if num % 2 == 0 else "odd"]
    print(f"Properties (even/odd): {properties}")  # Debugging: Print even/odd property
    
    # Armstrong check
    num_length = len(str(abs(num)))
    digit_powers_sum = sum(int(digit) ** num_length for digit in str(abs(num)))
    if num == digit_powers_sum:
        properties.insert(0, "armstrong")
        print(f"Armstrong check passed: {num} is an Armstrong number")  # Debugging: Print Armstrong result
    
    # Perfect number check (handle 0 case)
    is_perfect = num > 0 and sum(i for i in range(1, int(num ** 0.5) + 1) if num % i == 0) == num
    print(f"Perfect number check: {is_perfect}")  # Debugging: Print perfect number result
    
    # Prime check (basic implementation)
    if num > 1:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
    else:
        is_prime = False
    print(f"Prime check: {is_prime}")  # Debugging: Print prime check result
    
    # Fun fact (replace with NumbersAPI later)
    fun_fact = f"{num} is just an interesting number!"
    print(f"Fun fact: {fun_fact}")  # Debugging: Print fun fact
    
    # Return the response
    response = {
        "number": num,
        "is_prime": is_prime,
        "is_perfect": is_perfect,
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": fun_fact
    }
    print(f"Final response: {response}")  # Debugging: Print the final response
    return response

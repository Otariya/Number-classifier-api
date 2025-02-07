from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
app = FastAPI()
def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def is_perfect(n: int) -> bool:
    """Check if a number is perfect."""
    if n < 1:
        return False
    return sum(i for i in range(1, n) if n % i == 0) == n
@app.get("/api/classify-number")
def classify_number(number: str):
    try:
        num = float(number)  # Allow floating-point numbers
        if num.is_integer():  # Convert float 3.0 to int 3
            num = int(num)
        else:
            return JSONResponse(
                status_code=200,  # Floats should return 200, not 400
                content={
                    "number": num,
                    "is_prime": False,
                    "is_perfect": False,
                    "properties": ["floating-point"],
                    "digit_sum": None,
                    "fun_fact": "Fun facts are only available for whole numbers."
                },
            )
    except ValueError:
        return JSONResponse(
            status_code=400,  # Invalid input should return 400
            content={"error": True, "message": "Invalid input. Please provide a valid number."},
        )
    # Determine properties
    properties = ["even" if num % 2 == 0 else "odd"]
    # Check Armstrong number
    digit_powers_sum = sum(int(digit) ** len(str(abs(num))) for digit in str(abs(num)))
    if num == digit_powers_sum:
        properties.insert(0, "armstrong")
    # Construct response
    response = {
        "number": num,
        "is_prime": is_prime(num),
        "is_perfect": is_perfect(num),
        "properties": properties,
        "digit_sum": sum(int(digit) for digit in str(abs(num))),
        "fun_fact": f"{num} is just an interesting number!",
    }
    return JSONResponse(status_code=200, content=response)  # Ensure 200 status
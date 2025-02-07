from fastapi import FastAPI, HTTPException
import requests
import os  # Import os module to get PORT from environment
import uvicorn  # Import uvicorn to run the app

app = FastAPI()

def is_armstrong(num: int) -> bool:
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return num == sum(d**power for d in digits)

def get_fun_fact(number: int) -> str:
    response = requests.get(f"http://numbersapi.com/{number}/math")
    return response.text if response.status_code == 200 else "No fact available."

@app.get("/api/classify-number")
def classify_number(number: int):
    try:
        properties = []
        if number % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")

        if is_armstrong(number):
            properties.insert(0, "armstrong")

        fun_fact = get_fun_fact(number)
        digit_sum = sum(int(d) for d in str(number))

        return {
            "number": number,
            "is_prime": number > 1 and all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)),
            "is_perfect": number == sum(i for i in range(1, number) if number % i == 0),
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid input")

# This part ensures the app runs on the correct port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT is not set
    uvicorn.run(app, host="0.0.0.0", port=port)

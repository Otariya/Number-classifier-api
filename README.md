
# Number Classification API

## Overview
This FastAPI project provides an endpoint to classify numbers based on various mathematical properties. The API determines if a number is prime, perfect, Armstrong, and whether it is odd or even. It also calculates the digit sum and provides a fun fact about the number using an external API.

## Features
- Accepts **GET** requests with a number parameter.
- Classifies numbers based on:
  - **Prime status** (true/false)
  - **Perfect number status** (true/false)
  - **Armstrong number check**
  - **Odd or even classification**
  - **Digit sum calculation**
- Fetches a fun fact about the number from [NumbersAPI](http://numbersapi.com/).
- Returns structured JSON responses.
- Proper input validation and error handling.
- Fast response time (<500ms).

---
## API Documentation
### **Base URL**
```
http://localhost:8000/api
```
Or, if deployed:
```
https://your-deployed-url.com/api
```

### **Endpoints**
#### **1️⃣ Classify a Number**
**GET** `/api/classify-number`

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `number`  | `int` | ✅ Yes | The number to classify |

**Example Request:**
```
GET /api/classify-number?number=7
```

**Example Response:**
```json
{
  "number": 7,
  "is_prime": true,
  "is_perfect": false,
  "properties": ["armstrong", "odd"],
  "digit_sum": 7,
  "fun_fact": "7 is the smallest number of sides of a regular polygon that is not constructible by straightedge and compass."
}
```

**Response Codes:**
| Status Code | Description |
|------------|-------------|
| `200 OK`   | Successful response |
| `400 Bad Request` | Invalid input (e.g., missing `number` parameter) |
| `500 Internal Server Error` | Unexpected error |

---
## Setup and Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/number-classification-api.git
cd number-classification-api
```

### **2️⃣ Create and Activate a Virtual Environment**
```sh
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```sh
uvicorn main:app --reload
```
- The API will be accessible at: **`http://127.0.0.1:8000`**
- Interactive API Docs: **`http://127.0.0.1:8000/docs`**

---
## Deployment
To deploy the API on a public server:
### **1️⃣ Using Docker**
```sh
docker build -t number-classifier-api .
docker run -p 8000:8000 number-classifier-api
```

### **2️⃣ Deploying on Render or Railway**
- Push your code to GitHub.
- Connect the repo to a deployment service like Render or Railway.
- Set the `PORT` environment variable to `8000`.
- Deploy and get your live API URL.

---
## Code Structure
```
number-classification-api/
├── main.py  # API logic
├── requirements.txt  # Dependencies
├── README.md  # Project documentation
├── .gitignore  # Git ignored files
```

---
## Contributing
- Fork the repository.
- Create a new feature branch.
- Commit changes and push.
- Submit a Pull Request.

---
## License
MIT License © 2025 Otariyah


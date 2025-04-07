
# 🧪 Automated API Testing for E-commerce Backend

This project demonstrates an automated API testing suite for an e-commerce backend using Python, `requests`, and `pytest`. It validates core functionalities like authentication, product retrieval, cart operations, and order placement.

## 📌 Features Tested
- ✅ User Login Authentication
- 📦 Product Retrieval
- 🛒 Cart Management
- 📤 Order Placement

## 🧰 Tech Stack
- **Languages**: Python
- **Libraries**: `requests`, `pytest`
- **Tools**: Postman (for manual testing), Git, GitHub

## 📁 Project Structure

```
ecommerce-api-testing/
│
├── requirements.txt        # All dependencies
├── README.md               # Project overview
└── tests/
    └── test_auth.py        # Login auth test
```

## 🔍 Example Test Case

```python
def test_login_success():
    payload = {
        "username": "mor_2314",
        "password": "83r5^_"
    }
    response = requests.post("https://fakestoreapi.com/auth/login", json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
```

## 🚀 How to Run

1. **Clone the repo**:
   ```bash
   git clone https://github.com/MOHAMMAD-KAVISH/ecommerce-api-testing-sdet.git
   cd ecommerce-api-testing-sdet
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run tests**:
   ```bash
   pytest
   ```

## 📚 Sample APIs Used

This project uses [https://fakestoreapi.com](https://fakestoreapi.com) — a free dummy e-commerce REST API for testing and prototyping.

## 🎯 What I Learned

- Writing clean and modular test cases with `pytest`
- Making REST calls and parsing JSON responses using `requests`
- Validating API responses with assertions
- Using Postman for initial API exploration
- Version control with Git & GitHub

## 🤝 Author

Made with ❤️ by **Mohammad Kavish**  
📌 Role: SDET (Software Development Engineer in Test)  
🔗 [GitHub Profile](https://github.com/MOHAMMAD-KAVISH)
```

---

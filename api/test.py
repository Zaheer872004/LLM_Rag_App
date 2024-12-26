import requests

def test_finance_endpoint():
    url = "http://localhost:8000/chat/finance/invoke"
    payload = {"input_text": "Test message for finance"}
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Test the endpoint
response = test_finance_endpoint()
print(response)
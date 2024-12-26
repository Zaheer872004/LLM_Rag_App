import requests

def test_healthcare_endpoint():
    url = "http://localhost:8000/chat/healthcare/playground/"
    payload = {
        "input": {
            "input_text": "Test message for healthcare"
        }
    }  # Updated payload structure

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response from the server
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Handle specific HTTP errors
        print(f"Response content: {response.content}")  # Print response content for debugging
        return {"error": str(http_err)}
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")  # Handle other request errors
        return {"error": str(req_err)}

# Test the healthcare endpoint
response = test_healthcare_endpoint()
print(response)
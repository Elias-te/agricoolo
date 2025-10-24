import requests
from decouple import config

BASE_URL = config("https://developer.go.ke/")
CLIENT_ID = config("qWFQrkS9CssRuP3poTYApeWps4wf1AomHNG1sOkZIBXrZH4a")
CLIENT_SECRET = config("PAFtH5AxwZn82STvwkjJHHvMgAyCe8t1hfT23PbNQYMzruCzCX5LhwEqSpCIGfOv")

def get_access_token():
    """Fetch OAuth token from GavaConnect"""
    url = f"{BASE_URL}/oauth/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code == 200:
            return response.json().get("access_token")
    except Exception as e:
        print("Error getting GavaConnect token:", e)
    return None


def verify_kra_pin(kra_pin):
    """Verify KRA PIN via GavaConnect API"""
    token = get_access_token()
    if not token:
        print("Failed to get GavaConnect token.")
        return False

    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/kra/verify-pin?pin={kra_pin}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # GavaConnect typically returns {"status": "success", "valid": True/False, "details": {...}}
            return data.get("valid", False)
        else:
            print("KRA API error:", response.text)
    except Exception as e:
        print("Error verifying KRA PIN:", e)
    return False

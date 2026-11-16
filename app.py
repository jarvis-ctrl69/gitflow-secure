import os

def get_api_key():
    return os.getenv("DEMO_API_KEY", "")

def order_total(price, quantity):
    if price < 0 or quantity <= 0:
        raise ValueError("Price must be non-negative and quantity must be positive.")
    return price * quantity
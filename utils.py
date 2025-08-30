import pandas as pd
import numpy as np

def load_data():
    # Your inventory, usage, months, etc.
    data = {
        "Item": ["Chicken Breast", "Beef", "Rice", "Milk", "Lettuce", "Eggs", "Cheese", "Tomatoes", "Fish", "Yogurt"],
        "Category": ["Meat", "Meat", "Grain", "Dairy", "Vegetable", "Dairy", "Dairy", "Vegetable", "Meat", "Dairy"],
        "Location": ["Downtown", "Downtown", "Uptown", "Uptown", "Downtown", "Downtown", "Uptown", "Uptown", "Downtown", "Uptown"],
        "Beginning Inventory": [50, 40, 10, 30, 20, 60, 25, 15, 20, 35]
    }
    df = pd.DataFrame(data)
    return df

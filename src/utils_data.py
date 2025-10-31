# =========================================================
# utils_data.py  – Version with core helper functions
# =========================================================

from pathlib import Path
import pandas as pd
import numpy as np


# =====================================================================
# Helper Functions
# =====================================================================

# ---------------------------------------------------------
# 1. Load Dataset
# ---------------------------------------------------------
def load_real_dataset(path: Path) -> pd.DataFrame:
    """Load and validate the Historical Product Demand dataset."""
    df = pd.read_csv(path)
    required_cols = {'Product_Code', 'Warehouse', 'Product_Category', 'Date', 'Order_Demand'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Missing required columns. Found: {df.columns.tolist()}")
    print(f"Loaded dataset with {df.shape[0]:,} rows and {df['Warehouse'].nunique()} unique warehouses.")
    return df


# ---------------------------------------------------------
# 2. Extract Unique Warehouse Codes
# ---------------------------------------------------------
def get_unique_warehouses(df: pd.DataFrame) -> list:
    """Extract and return unique warehouse codes."""
    warehouses = sorted(df['Warehouse'].unique())
    print(f"Detected {len(warehouses)} warehouses: {warehouses[:10]}{'...' if len(warehouses) > 10 else ''}")
    return warehouses


# ---------------------------------------------------------
# 3. Generate a List of Coordinates For Each Warehouse
# ---------------------------------------------------------
def generate_city_coordinates(n: int) -> list:
    """
    Generate a list of coordinates (Spain-style) for each warehouse.
    Randomly picks from known Spanish cities or generates nearby points.
    """
    base_coords = [
        (40.42, -3.70),  # Madrid
        (41.38, 2.17),   # Barcelona
        (37.38, -5.99),  # Seville
        (39.47, -0.38),  # Valencia
        (43.26, -2.93),  # Bilbao
        (36.72, -4.42),  # Malaga
        (38.99, -1.86),  # Albacete
        (42.24, -8.72),  # Vigo
        (40.97, -5.66),  # Salamanca
        (39.86, -4.03)   # Toledo
    ]
    coords = [base_coords[i % len(base_coords)] for i in range(n)]
    return coords


# ---------------------------------------------------------
# 4. Generate Synthetic Points For Each Warehouse
# ---------------------------------------------------------
def generate_route_data(warehouses: list, coords: list, customers_per_warehouse: int = 3) -> pd.DataFrame:
    """Generate synthetic customer delivery points for each warehouse."""
    df_routes = pd.DataFrame([
        {
            "Warehouse": wh,
            "Customer_ID": f"{wh}_CUST_{i}",
            "Latitude": round(lat + np.random.uniform(-0.05, 0.05), 4),
            "Longitude": round(lon + np.random.uniform(-0.05, 0.05), 4),
            "Demand": np.random.randint(50, 250),
            "Vehicle_Capacity": 500,
            "Priority_Level": np.random.choice(["High", "Medium", "Low"], p=[0.2, 0.5, 0.3]),
            "Traffic_Condition": np.random.choice(["Low", "Medium", "High"], p=[0.4, 0.4, 0.2])
        }
        for wh, (lat, lon) in zip(warehouses, coords)
        for i in range(1, customers_per_warehouse + 1)
    ])

    print(f"Generated {len(df_routes)} route records for {len(warehouses)} warehouses.")
    return df_routes


# ---------------------------------------------------------
# 5. Save the Synthetic Dataset
# ---------------------------------------------------------
def save_dataset(df: pd.DataFrame, path: Path):
    """Save the synthetic dataset to a CSV file."""
    df.to_csv(path, index=False)
    print(f"Saved dataset to {path.resolve()}")
    print(df.head(10))



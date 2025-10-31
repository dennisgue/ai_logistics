# src/preprocess_main.py
from pathlib import Path
from utils_data import (
    load_real_dataset,
    get_unique_warehouses,
    generate_city_coordinates,
    generate_route_data,
    save_dataset,
)

# Detect data directory
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"

if __name__ == "__main__":
    print(" Starting preprocessing pipeline...")

    # 1️.Load historical dataset
    df = load_real_dataset(DATA_DIR / "Historical_Product_Demand.csv")

    # 2️.Extract warehouses
    warehouses = get_unique_warehouses(df)

    # 3️.Generate coordinates and routes
    coords = generate_city_coordinates(len(warehouses))
    df_routes = generate_route_data(warehouses, coords)

    # 4️.Save synthetic routes
    save_dataset(df_routes, DATA_DIR / "Warehouse_Route_Planning.csv")

    print("Pipeline completed successfully!")

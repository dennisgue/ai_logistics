# =========================================================
# Preprocessing Pipeline - Updated for New Folder Structure
# =========================================================

from pathlib import Path
from utils_data import (
    load_real_dataset,
    get_unique_warehouses,
    generate_city_coordinates,
    generate_route_data,
    save_dataset,
)

# ---------------------------------------------------------
# Project and Data Directory Setup
# ---------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"

if __name__ == "__main__":
    print("Starting preprocessing pipeline...")

    # 1.Load historical dataset (from raw data folder)
    df = load_real_dataset(RAW_DATA_DIR / "Historical_Product_Demand.csv")

    # 2️.Extract unique warehouses
    warehouses = get_unique_warehouses(df)

    # 3️.Generate coordinates and synthetic route data
    coords = generate_city_coordinates(len(warehouses))
    df_routes = generate_route_data(warehouses, coords)

    # 4️.Save synthetic route data to the raw data folder
    save_dataset(df_routes, PROCESSED_DATA_DIR / "Warehouse_Route_Planning.csv")

    print("Pipeline completed successfully!")


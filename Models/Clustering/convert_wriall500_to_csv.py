import os
import sys
import geopandas as gpd
import pandas as pd

def find_shapefile():
    candidates = [
        os.path.join(os.getcwd(), "River_Outlines _SHP:KMZ)", "wriall500.shp"),
        os.path.join(os.getcwd(), "wriall500.shp"),
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def main():
    shp_path = None
    if len(sys.argv) > 1:
        shp_path = sys.argv[1]
    else:
        shp_path = find_shapefile()
    if shp_path is None:
        raise FileNotFoundError("wriall500.shp not found")
    gdf = gpd.read_file(shp_path)
    df = gdf.drop(columns=["geometry"])
    out_csv = os.path.join(os.getcwd(), "wriall500.csv")
    df.to_csv(out_csv, index=False)
    print(out_csv)
    print(len(df))
    print(",".join(df.columns))
    print(df.head().to_string())

if __name__ == "__main__":
    main()

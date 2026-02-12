import os
import geopandas as gpd
import pandas as pd

def to_csv(kml_path, out_name):
    gdf = gpd.read_file(kml_path, driver="KML")
    df = gdf.drop(columns=["geometry"])
    out_csv = os.path.join(os.getcwd(), out_name)
    df.to_csv(out_csv, index=False)
    return out_csv, len(df), list(df.columns)

def main():
    base = os.getcwd()
    kml_dir = os.path.join(base, "Dams_n_Lakes")
    files = [
        "1DrainageRegions_SouthAfrica__doc.kml",
        "2Rivers__doc.kml",
        "3dams__dams.kml",
        "4Quaterly__hca_4-geo_codes.kml",
        "5Legend_Maucha__Legend_Maucha.kml",
    ]
    for name in files:
        p = os.path.join(kml_dir, name)
        if os.path.exists(p):
            out = f"{os.path.splitext(name)[0]}.csv"
            csv_path, rows, cols = to_csv(p, out)
            print(csv_path)
            print(rows)
            print(",".join(cols))

if __name__ == "__main__":
    main()

import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw")
PROCESSED_DATA = Path("data/processed")


def load_excel_files():
    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)

    files = list(RAW_DATA.glob("*.xlsx"))

    if not files:
        print("No Excel files found in data/raw")
        return

    for file in files:
        df = pd.read_excel(file)

        output = PROCESSED_DATA / file.with_suffix(".csv").name

        df.to_csv(output, index=False)

        print(f"Processed: {file.name}")


if __name__ == "__main__":
    load_excel_files()
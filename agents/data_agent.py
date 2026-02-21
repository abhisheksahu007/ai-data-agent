import pandas as pd
import numpy as np

try:
    import polars as pl
    POLARS_AVAILABLE = True
except ImportError:
    POLARS_AVAILABLE = False


class DataAgent:

    @staticmethod
    def load_data(file):

        size_mb = file.size / (1024 * 1024)

        encodings = ["utf-8", "latin1", "ISO-8859-1", "cp1252"]

        for enc in encodings:
            try:
                if size_mb > 50 and POLARS_AVAILABLE:
                    df = pl.read_csv(file, encoding=enc).to_pandas()
                else:
                    df = pd.read_csv(file, encoding=enc)

                return df

            except Exception:
                continue

        return pd.read_csv(file, encoding="latin1", low_memory=False)

    # ✅ THIS METHOD MUST EXIST
    @staticmethod
    def analyze(df):
        return {
            "rows": df.shape[0],
            "columns": df.shape[1],
            "numeric_cols": df.select_dtypes(include=np.number).columns.tolist(),
            "categorical_cols": df.select_dtypes(exclude=np.number).columns.tolist(),
            "missing_values": df.isnull().sum().to_dict()
        }
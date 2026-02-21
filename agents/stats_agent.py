from sklearn.ensemble import IsolationForest
import numpy as np

class StatsAgent:

    @staticmethod
    def summary(df):
        return df.describe().to_dict()

    @staticmethod
    def correlation(df):
        return df.corr(numeric_only=True)

    @staticmethod
    def outliers(df):
        num_df = df.select_dtypes(include=np.number)

        if num_df.empty:
            return {"outliers": 0}

        model = IsolationForest(contamination=0.05, random_state=42)
        preds = model.fit_predict(num_df.fillna(0))

        return {"outliers_detected": int((preds == -1).sum())}
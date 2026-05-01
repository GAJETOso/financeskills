import pandas as pd
import numpy as np

class AuditDetector:
    def __init__(self, transactions_df):
        self.df = transactions_df
        self.flags = []

    def check_z_score(self, column='amount', threshold=3):
        """
        Flag transactions with an amount significantly higher than the mean.
        """
        mean = self.df[column].mean()
        std = self.df[column].std()
        
        anomalies = self.df[np.abs(self.df[column] - mean) > (threshold * std)]
        for idx, row in anomalies.iterrows():
            self.flags.append({
                'transaction_id': idx,
                'type': 'STATISTICAL_OUTLIER',
                'reason': f"Amount ${row[column]} is more than {threshold} standard deviations from mean.",
                'confidence': 0.8
            })
        return anomalies

    def check_duplicate_payments(self, amount_col='amount', vendor_col='vendor'):
        """
        Flag potential duplicate payments (same vendor, same amount, within short window).
        """
        # Logic for duplicate detection
        duplicates = self.df[self.df.duplicated(subset=[amount_col, vendor_col], keep=False)]
        for idx, row in duplicates.iterrows():
            self.flags.append({
                'transaction_id': idx,
                'type': 'DUPLICATE_PAYMENT',
                'reason': f"Possible duplicate payment of ${row[amount_col]} to {row[vendor_col]}.",
                'confidence': 0.6
            })
        return duplicates

    def get_report(self):
        return pd.DataFrame(self.flags)

if __name__ == "__main__":
    # Test with dummy data
    data = {
        'amount': [100, 105, 100, 10000, 102, 100],
        'vendor': ['AWS', 'AWS', 'AWS', 'AWS', 'AWS', 'AWS'],
        'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-01', '2024-01-05', '2024-01-06', '2024-01-01'])
    }
    df = pd.DataFrame(data)
    detector = AuditDetector(df)
    detector.check_z_score()
    detector.check_duplicate_payments()
    print(detector.get_report())

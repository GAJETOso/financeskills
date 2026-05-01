import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_transactions(n=1000):
    vendors = ['AWS', 'Google Cloud', 'Slack', 'Office Depot', 'Starbucks', 'Uber', 'Zoom']
    data = []
    
    start_date = datetime(2023, 1, 1)
    
    for i in range(n):
        vendor = random.choice(vendors)
        # Normal transaction amount
        amount = round(random.uniform(10, 500), 2)
        
        # Inject some anomalies
        if i == 50: # Massive outlier
            amount = 25000.00
        if i == 100: # Duplicate pair part 1
            amount = 499.99
            vendor = 'Stripe'
        if i == 101: # Duplicate pair part 2
            amount = 499.99
            vendor = 'Stripe'
            
        date = start_date + timedelta(days=random.randint(0, 365))
        data.append({
            'transaction_id': f"TXN-{i:04d}",
            'date': date,
            'vendor': vendor,
            'amount': amount,
            'category': 'Operations'
        })
        
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = generate_transactions()
    df.to_csv('projects/audit-system/data/raw_transactions.csv', index=False)
    print(f"Generated {len(df)} transactions in data/raw_transactions.csv")

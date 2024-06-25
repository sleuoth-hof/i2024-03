import pandas as pd
from datetime import datetime, timedelta


def delete_old_newses():
    df = pd.read_csv('newsDataBase.csv')
    df['formatted_date'] = pd.to_datetime(df['formatted_date'])
    now = datetime.utcnow()
    cutoff_date = now - timedelta(days=1)
    filtered_df = df[df['formatted_date'] >= cutoff_date]
    filtered_df.to_csv('filtered_file.csv', index=False)


delete_old_newses()

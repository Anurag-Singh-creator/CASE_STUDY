import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def get_trade_code_clusters(df, n_clusters=3, random_state=42):
    """
    Clusters trade codes based on mean/std of price and bookings.
    
    Parameters:
    - df: DataFrame with columns ['trade_code', 'price', 'bookings']
    - n_clusters: number of clusters to use in KMeans
    - random_state: seed for reproducibility
    
    Returns:
    - Dictionary mapping trade_code to assigned cluster
    """
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()

    # Aggregate trade-level features
    summary_df = (
        df.groupby('trade_code')
          .agg(
              mean_price=('price', 'mean'),
              std_price=('price', 'std'),
              mean_bookings=('bookings', 'mean'),
              std_bookings=('bookings', 'std')
          )
    )

    # Prepare features
    features = summary_df[['mean_price', 'std_price', 'mean_bookings', 'std_bookings']]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    summary_df['cluster'] = kmeans.fit_predict(scaled_features)

    # Return dictionary of trade_code -> cluster
    return summary_df['cluster'].to_dict()

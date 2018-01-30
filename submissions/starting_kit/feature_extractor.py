
class FeatureExtractor():
    
    def __init__(self):
        pass

    def fit(self, X_df, y=None):
        return self

    def fit_transform(self, X_df, y=None):
        self.fit(X_df)
        return self.transform(self.X_df)

    def transform(self, X_df):
        return X_df[['latitude', 'longitude']].values
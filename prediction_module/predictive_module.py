from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(df_history):
    X = df_history[['Total Credits']].values
    y = df_history['CGPA'].values
    model = LinearRegression().fit(X, y)
    return model

def predict_future_cgpa(model, future_credits):
    return round(model.predict(np.array([[future_credits]]))[0], 2)

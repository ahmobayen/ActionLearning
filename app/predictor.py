import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt

def load_model(model_name):
    return tf.keras.models.load_model(f'./models/{model_name}.h5')

def make_prediction(test_data, model):
    # Perform any preprocessing of the test_data if needed
    predictions = model.predict(test_data)
    return pd.DataFrame(predictions, columns=["Predicted"])

def prediction_chart(prediction_data, original_data):
    plt.figure(figsize=(12, 6))
    plt.plot(original_data["Date"], original_data["Close"], label="Original Data")
    plt.plot(prediction_data["Date"], prediction_data["Predicted"], label="Predicted Data")
    plt.xlabel("Date")
    plt.ylabel("Stock Price")
    plt.title("Stock Price Prediction")
    plt.legend()
    plt.show()

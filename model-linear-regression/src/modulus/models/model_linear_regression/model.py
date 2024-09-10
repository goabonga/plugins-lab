import joblib
from sklearn.linear_model import LinearRegression

from modulus.library.models import ModelInterface

class LinearRegressionModel(ModelInterface):
    def __init__(self):
        self.model = None

    def extract(self, data):
        """
        Extracts data. Here, data is expected to be a numpy array.
        For real-world scenarios, this might involve reading from a database or file.
        """
        return data

    def transform(self, data):
        """
        Transforms the data. This could include feature scaling, encoding, etc.
        For simplicity, this example assumes data is already in the correct format.
        """
        X = data[:, :-1]  # Features
        y = data[:, -1]  # Target variable
        return X, y

    def load(self, X, y):
        """
        Loads the transformed data for training.
        """
        return X, y

    def train(self, X, y):
        """
        Trains a simple linear regression model.
        """
        self.model = LinearRegression()
        self.model.fit(X, y)

    def predict(self, X):
        """
        Predicts using the trained model.
        """
        if self.model is None:
            raise ValueError("Model is not trained. Train the model first.")
        return self.model.predict(X)

    def save_model(self, filepath):
        """
        Saves the trained model to a file.
        """
        if self.model is None:
            raise ValueError("Model is not trained. Train the model first.")
        joblib.dump(self.model, filepath)

    def load_model(self, filepath):
        """
        Loads a model from a file.
        """
        self.model = joblib.load(filepath)

    def retrain(self, X, y):
        """
        Retrains the model from the loaded model state.
        """
        if self.model is None:
            raise ValueError("Model is not loaded. Load the model first.")
        self.model.fit(X, y)


# # Example usage:
# data = np.array([
#     [1, 2, 3, 4, 10],  # Example data rows
#     [2, 3, 4, 5, 15],
#     [3, 4, 5, 6, 20],
# ])
#
# linear_model = LinearRegressionModel()
# extracted_data = linear_model.extract(data)
# X, y = linear_model.transform(extracted_data)
# X, y = linear_model.load(X, y)
# linear_model.train(X, y)
# predictions = linear_model.predict(X)
# print(f"Predictions: {predictions}")
#
# # Save and load model
# linear_model.save_model("linear_model.pkl")
# linear_model.load_model("linear_model.pkl")
#
# # Retrain with new data
# linear_model.retrain(X, y)
#

from abc import ABC, abstractmethod


class ModelInterface(ABC):
    """
    🧠 ModelInterface - Abstract Base Class
    
    The `ModelInterface` is an abstract base class that defines the blueprint for your data extraction, 
    transformation, and machine learning workflows. This interface ensures that any implementing class 
    will adhere to a consistent structure and behavior for model lifecycle management.
    
    🚀 Overview:
    This class establishes a common protocol for implementing machine learning models by outlining 
    essential methods that every model should have. Each method is abstract and must be implemented 
    by any subclass.
    """

    @abstractmethod
    def extract(self, data):
        """
        🕵️‍♂️ extract(self, data)
        
        **Purpose:** Extracts data from a source. This is where you pull in the data required for your model.
        
        **Parameters:**
          - `data`: The source data to be extracted.
        
        **Returns:** Extracted data ready for transformation.
        """

    @abstractmethod
    def transform(self, data):
        """
        🔄 transform(self, data)
        
        **Purpose:** Transforms the extracted data. This method modifies the data into a format suitable for training.
        
        **Parameters:**
          - `data`: The data to be transformed.
        
        **Returns:** Transformed data ready for loading.
        """

    @abstractmethod
    def load(self, X, y):
        """
        📥 load(self, X, y)
        
        **Purpose:** Loads the transformed data for model training. It's the bridge between data transformation and model training.
        
        **Parameters:**
          - `X`: The feature set.
          - `y`: The target variable.
        
        **Returns:** Loaded data prepared for training.
        """

    @abstractmethod
    def train(self, X, y):
        """
        🏋️‍♂️ train(self, X, y)
        
        **Purpose:** Trains the model using the provided data. The heart of the machine learning process.
        
        **Parameters:**
          - `X`: The feature set.
          - `y`: The target variable.
        
        **Returns:** Trained model ready for predictions.
        """

    @abstractmethod
    def predict(self, X):
        """
        🔮 predict(self, X)
        
        **Purpose:** Makes predictions using the trained model. Time to see your model in action!
        
        **Parameters:**
          - `X`: The data on which predictions are to be made.
        
        **Returns:** Predictions made by the model.
        """

    @abstractmethod
    def save_model(self, filepath):
        """
        💾 save_model(self, filepath)
        
        **Purpose:** Saves the trained model to a file. Don't forget to save your hard work!
        
        **Parameters:**
          - `filepath`: The path where the model will be saved.
        
        **Returns:** None
        """

    @abstractmethod
    def load_model(self, filepath):
        """
        📂 load_model(self, filepath)
        
        **Purpose:** Loads the model from a file. Revive your saved models from the disk.
        
        **Parameters:**
          - `filepath`: The path from which the model will be loaded.
        
        **Returns:** Loaded model ready to make predictions.
        """

    @abstractmethod
    def retrain(self, X, y):
        """
        🔄 retrain(self, X, y)
        
        **Purpose:** Retrains the model using new data. Keep your model fresh and up-to-date with the latest data!
        
        **Parameters:**
          - `X`: The new feature set.
          - `y`: The new target variable.
        
        **Returns:** Retrained model with updated knowledge.
        """

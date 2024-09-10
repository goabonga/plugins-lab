# model-linear-regression/src/modulus/models/model_linear_regression/__init__.py
from typing import Literal

from pydantic import BaseModel, Field


class LinearRegressionRequest(BaseModel):
    class_name: Literal["decision_tree"] = Field(
        default="decision_tree",
        alias="model_name",
    )
    values: list[str] = Field(
        ..., description="Input values for Linear Regression model"
    )


class LinearRegressionResponse(BaseModel):
    # Define the response fields as needed
    message: str = Field(..., description="Response message")
    data: dict = Field(..., description="Prediction result data")


modelRequest = LinearRegressionRequest
modelResponse = LinearRegressionResponse

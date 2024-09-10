from typing import Literal

from pydantic import BaseModel, Field


class DecisionTreeRequest(BaseModel):
    class_name: Literal["decision_tree"] = Field(
        default="decision_tree",
        alias="model_name",
    )
    values: list[str] = Field(..., description="Input values for Decision Tree model")


class DecisionTreeResponse(BaseModel):
    # Define the response fields as needed
    message: str = Field(..., description="Response message")
    data: dict = Field(..., description="Prediction result data")


modelRequest = DecisionTreeRequest
modelResponse = DecisionTreeResponse

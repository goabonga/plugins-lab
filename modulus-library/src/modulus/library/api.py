import pkgutil
import importlib
import logging
from typing import Annotated, Dict, Type, Union

import modulus.models
from fastapi import Body, FastAPI, HTTPException
from pydantic import BaseModel

# Setup FastAPI app
app = FastAPI(
    title="Modulus Prediction API",
    description="🚀 API for validating and predicting using dynamically discovered Pydantic models.",
    version="1.0.0",
)


# Initialize logger
def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


setup_logging()


def models_discovery(namespace):
    return [
        name
        for _, name, _ in pkgutil.iter_modules(
            namespace.__path__, namespace.__name__ + "."
        )
    ]

# Dictionaries to hold the dynamically loaded request and response schemas
model_request_schemas: Dict[str, Type[BaseModel]] = {}
model_response_schemas: Dict[str, Type[BaseModel]] = {}


def load_model_schemas():
    """
    🔍 Discover and Load Pydantic Model Schemas.

    This function discovers available Pydantic `ModelRequest` and `ModelResponse` schemas
    in the framework's models and loads them into the application.
    """
    models_list = models_discovery(modulus.models)
    logging.info(f"🧩 Discovered models: {models_list}")

    for model_name in models_list:
        try:
            # Attempt to import the model's module
            module = importlib.import_module(f"{model_name}")

            # Normalize model name for consistent key naming
            normalized_model_name = model_name.lower().replace(".", "_")

            # Check for a `ModelRequest` class in the module
            model_request = getattr(module, "modelRequest", None)
            if model_request and issubclass(model_request, BaseModel):
                model_request_schemas[normalized_model_name] = model_request
                logging.info(
                    f"✅ Successfully registered ModelRequest for {normalized_model_name}."
                )
            else:
                logging.error(f"⚠️ No Pydantic ModelRequest found in {model_name}.")

            # Check for a `ModelResponse` class in the module
            model_response = getattr(module, "modelResponse", None)
            if model_response and issubclass(model_response, BaseModel):
                model_response_schemas[normalized_model_name] = model_response
                logging.info(
                    f"✅ Successfully registered ModelResponse for {normalized_model_name}."
                )
            else:
                logging.error(f"⚠️ No Pydantic ModelResponse found in {model_name}.")

        except ModuleNotFoundError:
            logging.error(f"❌ Model module {model_name} not found.")
        except Exception as e:
            logging.error(f"❌ Error loading model {model_name}: {e}")


# Load all discovered Pydantic schemas
load_model_schemas()

# Create Union types for both requests and responses
ModelRequestUnion = Union[tuple(model_request_schemas.values())]
ModelResponseUnion = Union[tuple(model_response_schemas.values())]

# Define Annotated types for enhanced validation and OpenAPI documentation
AnnotatedModelRequest = Annotated[
    ModelRequestUnion,
    Body(
        ...,
        description="Request body that validates against one of the discovered ModelRequest schemas.",
        example={"model_name": "linear_regression", "values": ["value1", "value2"]},
    ),
]


@app.post("/predict", response_model=ModelResponseUnion)
async def predict(request: AnnotatedModelRequest):
    """
    🎯 Predict Endpoint to Validate and Process Requests.

    This endpoint dynamically validates the incoming request using
    the appropriate `ModelRequest` schema for the specified model
    and returns a response validated against the corresponding `ModelResponse`.

    🛠️ Returns:
        - A mock prediction response if validation is successful.
    """
    # Extract the matched model name, normalize it to the schema's naming convention
    #
    ## Validate that the matched model has corresponding schemas
    # model_request_schema = model_request_schemas.get(matched_model_name)
    # if not model_request_schema or not isinstance(request, model_request_schema):
    #    raise HTTPException(status_code=400, detail="Request does not match any known schema")
    #
    normalize_response_model_name = next(
        (key for key in model_response_schemas if request.model_name in key), None
    )

    response_schema = model_response_schemas.get(normalize_response_model_name)

    if not response_schema:
        raise HTTPException(
            status_code=500, detail="No corresponding ModelResponse schema found"
        )

    logging.info(f"🔍 Successfully validated request for {request.model_name}.")

    # Mock prediction logic (replace with actual model prediction logic)
    mock_response_data = {
        "message": f"Prediction successful for {request.model_name}",
        "data": request.dict(),
    }

    # Create an instance of the response schema with the mock data
    response = response_schema(**mock_response_data)

    return response


def main():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

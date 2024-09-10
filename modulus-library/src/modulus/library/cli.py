import pkgutil
import importlib
import inspect
import logging
from typing import Dict, Type

import click
import modulus.models
from pydantic import BaseModel

from modulus.library.models import ModelInterface


def setup_logging():
    """Sets up the logging configuration."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


@click.group()
def cli():
    """Main application command group."""
    logging.info("Application started.")


# Dictionaries to hold the dynamically loaded request and response schemas
model_request_schemas: Dict[str, Type[BaseModel]] = {}
model_response_schemas: Dict[str, Type[BaseModel]] = {}


def models_discovery(namespace):
    return [
        name
        for _, name, _ in pkgutil.iter_modules(
            namespace.__path__, namespace.__name__ + "."
        )
    ]

def discover_model_classes(module):
    """
    Discover classes implementing ModelInterface in the given module.

    :param module: The module to inspect.
    :return: List of classes implementing ModelInterface.
    """
    model_classes = []
    for name, obj in inspect.getmembers(module, inspect.isclass):
        # Check if the class is a subclass of ModelInterface but not ModelInterface itself
        if issubclass(obj, ModelInterface) and obj is not ModelInterface:
            model_classes.append(obj)
    return model_classes


def create_command_for_method(model_instance, method_name):
    """
    Creates a click command for a given method of a model instance.

    :param model_instance: The instance of the model class.
    :param method_name: The name of the method to expose as a command.
    :return: A click command function.
    """
    method = getattr(model_instance, method_name)

    @click.command(name=method_name)
    @click.argument("args", nargs=-1)
    def command(args):
        """Dynamically generated command for model methods."""
        # Assuming all methods take data as a single argument for simplicity
        result = method(*args)
        click.echo(f"Result of {method_name}: {result}")

    return command


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
            module = importlib.import_module(f"{model_name}.model")

            # Discover classes implementing ModelInterface
            model_classes = discover_model_classes(module)
            if not model_classes:
                logging.warning(f"No ModelInterface classes found in {model_name}.")
                continue

            # Iterate over discovered model classes and create commands
            for model_class in model_classes:

                model_instance = (
                    model_class()
                )  # Assuming the class can be instantiated without arguments
                command_group = click.Group(name=model_class.__name__)

                # Dynamically add methods as subcommands to the group
                for method_name in dir(model_instance):
                    # Check if the attribute is a method and not private
                    if callable(
                        getattr(model_instance, method_name)
                    ) and not method_name.startswith("_"):
                        command = create_command_for_method(model_instance, method_name)
                        command_group.add_command(command)

                # Register the command group with the main click group
                cli.add_command(command_group)
                logging.info(
                    f"✅ Successfully registered command group for {model_class.__name__}."
                )

        except ModuleNotFoundError:
            logging.error(f"❌ Model module {model_name} not found.")
        except Exception as e:
            logging.error(f"❌ Error loading model {model_name}: {e}")


def main():
    setup_logging()
    # Load all discovered Pydantic schemas and model commands
    load_model_schemas()
    cli()

import platform
import subprocess


import fastapi
import numpy
import tensorflow
import keras


from ..schema import response_schema


def get_backend_information():
    CURRENT_COMMIT = ""
    try:
        CURRENT_COMMIT = subprocess.run(["git", "describe", "--always"], capture_output=True).stdout.decode().strip()
    except Exception as exception:
        print(exception)

    SYSTEM_SPEC = ""
    try:
        SYSTEM_SPEC = subprocess.run(["cat", "/etc/os-release"], capture_output=True).stdout.decode().strip()
    except Exception as exception:
        print(exception)

    return response_schema.BackendInformationOut(
        current_commit=CURRENT_COMMIT,
        system_spec=SYSTEM_SPEC,
        fastapi_version=fastapi.__version__,
        python_version=platform.python_version(),
        numpy_version=numpy.__version__,
        tensorflow_version=tensorflow.__version__,
        keras_version=keras.__version__,
    )

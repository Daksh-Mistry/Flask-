'''
This is Custom Exception File, change anything here for Exception Handling in whole project

Basic Usage guide of this file is as follow:
    from ML_Project.exception import CustomException
    try:
    ...
    except Exception as e:
        raise CustomException(e) # Use This to Handle Errors in any code snippet
'''




import sys
from typing import Any


class CustomException(Exception):
    """Custom exception for the ML project with traceable error context."""

    def __init__(self, error_message: Any, error_detail: Any = None):
        if error_detail is None or error_detail is sys:
            error_detail = sys.exc_info()
        self.error_message = self._format_error_message(error_message, error_detail)
        super().__init__(self.error_message)
        self.error_detail = error_detail

    def _format_error_message(self, error_message: Any, error_detail: Any) -> str:
        _, _, exc_tb = error_detail
        if exc_tb is not None:
            frame = exc_tb.tb_frame
            file_name = frame.f_code.co_filename
            line_number = exc_tb.tb_lineno
            return (
                f"Error occurred in script: [{file_name}] at line number: [{line_number}] "
                f"message: [{error_message}]"
            )

        return f"Error message: [{error_message}]"

    def __str__(self) -> str:
        return str(self.error_message)


def raise_custom_exception(error: Any, error_detail: Any = None) -> None:
    """Helper to raise the custom exception with captured traceback."""
    raise CustomException(error, error_detail)

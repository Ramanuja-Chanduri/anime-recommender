import sys

class CustomException(Exception):
    def __init__(self, message: str, error_detail: Exception=None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

    @staticmethod
    def get_detailed_error_message(message, error_detail):
        _, _, ex_tb = sys.exc_info()
        file_name = ex_tb.tb_frame.f_code.co_filename if ex_tb else "Unknown File"
        line_number = ex_tb.tb_lineno if ex_tb else "Unknown Line"
        return f"{message} | Error: {error_detail} | File: {file_name} | Line: {line_number}"
    
    def __str__(self):
        return self.error_message
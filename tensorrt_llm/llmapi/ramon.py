import inspect
import os

def log(msg: str):
    caller_frame = inspect.stack()[1]
    info = inspect.getframeinfo(caller_frame.frame)

    filename = os.path.basename(info.filename)
    line_number = info.lineno
    function_name = info.function

    # Determine class name if applicable
    class_name = None
    if 'self' in caller_frame.frame.f_locals:
        class_name = caller_frame.frame.f_locals['self'].__class__.__name__
    elif 'cls' in caller_frame.frame.f_locals:
        class_name = caller_frame.frame.f_locals['cls'].__name__

    print(f"XXXXX::{filename}::{class_name}::{function_name}::{line_number}::{msg}")
    return filename, class_name, function_name, line_number


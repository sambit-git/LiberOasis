import os

def clean_file_path(path):
    for symbol in ['"', "/", "\\", ":", "*", "|", "?", "<", ">"]:
        path = path.replace(symbol, "")
    return path.strip()

def upload_to(instance, filename):
    if hasattr(instance, "title"):
        prop = "title"
    elif hasattr(instance, "fullname"):
        prop = "fullname"
    else:
        raise NotImplemented(
            "this property is not implemented to work with uploads")
    _, ext = os.path.splitext(filename)
    name = clean_file_path(getattr(instance, prop))
    root = instance.__class__.__name__
    upload_path = f"{root}/{getattr(instance, prop)}{ext}"
    
    counter = 0
    while os.path.exists(upload_path):
        counter += 1
        upload_path = f"{root}/{getattr(instance, prop)}{counter}{ext}"
    return upload_path
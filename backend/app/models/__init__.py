import os

for file in os.listdir(os.path.dirname(__file__)):
    if not file.startswith("_"):
        module_name, _ = os.path.splitext(file)
        module = __import__(f"models.{module_name}", fromlist=[module_name])
        globals()[module_name] = module
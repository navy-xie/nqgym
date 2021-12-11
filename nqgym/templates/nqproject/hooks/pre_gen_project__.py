import re
import sys


MODULE_REGEX = r"^[a-zA-Z][_a-zA-Z0-9]+$"
module_name = "{{cookiecutter.package_name}}"

if not re.match(MODULE_REGEX, module_name):
    print(f"ERROR: '{module_name}' is a invalid Python module name.")
    sys.exit(1)

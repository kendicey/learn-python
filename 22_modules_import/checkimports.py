# to install a module, you run `pip install module_name` in terminal
import numpy
import sample
# import sampletext          # you cannot import a txt file as it is not a module
import json


import sys

sys.path.insert(
    1, r'C:\Users\kendi\Desktop\GitHub\learn-python\22_modules_import\Workplace')  # right-click on the folder to copy path

import trial    # IDE cannot read the path set but the compiler will know


print(trial.names)

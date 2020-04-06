# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from _datetime import date

import time


# today = datetime.date.today()
today = date.today()
print(today)

# timestamp = time.time()
timestamp = time()
print(timestamp)
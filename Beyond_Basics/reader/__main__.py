''' Basic project layout
project_name
|--- __main__.py
|--- project_name
|    |--- __init__.py
|    |--- more_source.py
|    |--- subpackage1
|    |    |--- __init__.py
|    |---test
|        |--- __init__.py
|        |--- test_code.py
|--- setup.py
'''


import sys
import os.path
import reader   

print(sys.argv) 
r = reader.Reader(sys.argv[1])
try:
    print(r.read())
finally:
    r.close()

print('executing __main__.py with name {}'.format(__name__))
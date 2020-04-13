import os
import sys

# Refer: https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
# Refer: https://stackoverflow.com/questions/4383571/importing-files-from-different-folder
import importlib, importlib.util

def module_from_file(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

cdown = module_from_file("cdown", "../src/cdown/__init__.py")
 
if __name__ == '__main__':
    year = sys.argv[1]
    var = sys.argv[2]

    try:
        ws = sys.argv[3]
    except:
        ws = os.path.join(os.curdir, year)

    cd = cdown.Cdown(year=year, ws=ws)

    cd.get(var)

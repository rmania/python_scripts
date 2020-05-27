# write a custom context manager with a class
class Open_File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    # set-up of our context Manager
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    # tear-down of our context Manager
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


# create file object within ContextManager (first line runs__init__ and __enter__)
with Open_File('sample.txt', mode='w') as f:
    f.write('testing')

print(f.closed) # should return True


#  write a custom context manager with a function
from contextlib import contextmanager
import os

@contextmanager
def open_file(file, mode):
    try:
        f = open(file, mode)
        yield f
    finally:
        f.close

with open_file('sample.txt', "w") as f:
    f.write("write bla")

# more practical example
@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally: # teardown
        os.chdir(cwd)

#usage:
with change_dir("example_dir1"):
    print(os.listdir())
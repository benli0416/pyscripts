import os
from os.path import join, getsize
for root, dirs, files in os.walk("d:\work\costupdate"):
    print root, dirs, files
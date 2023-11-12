import os
import sys

def resource_path(relative):
    # print("hasattr(sys,'_MEIPASS')", hasattr(sys, "_MEIPASS"))
    
    if hasattr(sys, "_MEIPASS"):
        print(sys._MEIPASS)
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)
from main import FarmAnalysis
from main import *

def run_example(*args,**kwargs):
    
    farm = FarmAnalysis(*args,**kwargs)
    
    analysis = farm.__main__(**kwargs)
                
if __name__ == "__main__":
    import sys
    
    run_example(*sys.argv[1:])
    
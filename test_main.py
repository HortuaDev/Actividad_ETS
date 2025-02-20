from io import StringIO
import sys
from main import main

def test_main():
    captured_output = StringIO()
    sys.stdout = captured_output
    
    main()
    
    sys.stdout = sys.__stdout__
    
    assert captured_output.getvalue().strip() == "Hola mundo"
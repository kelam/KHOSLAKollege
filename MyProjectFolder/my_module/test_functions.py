from functions import *

def test_check_college_input():
    test = CollegeProcess()
    test.check_college_input('Killmonger') 
    assert 'Killmonger' in test.college_choices

    

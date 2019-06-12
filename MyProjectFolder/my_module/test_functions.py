from functions import *

def test_CheckCollegeInput():
    test = CollegeProcess()
    test.check_college_input('Killmonger') 
    assert 'Killmonger' in test.college_choices

    
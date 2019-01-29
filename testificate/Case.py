from enum import Enum

# different types of test cases
class CaseType(Enum):
    EQUALS=0
    CONTAINS=1

# a class defining how a test case should behave
class Case:
    
    def __init__(self, case_type, filename="",lineno="",function="", passed=False):

        # type of test case (CaseType)
        self.case_type=case_type

        # filename where the case was instantiated 
        self.filename=filename
        # line number where the case was instantiated
        self.lineno=lineno
        # function name where the case was instantiated
        self.function=function

        # name of the test case, used to identify it
        self.name=function+" ~ "+str(case_type.name)+" -> "+filename+" at line "+str(lineno)
        # has the case passed
        self.passed=passed

    # magic method to print the test case
    def __str__(self):
        if self.passed:
            return "PASSED : "+self.name
        else:
            return "FAILED : "+self.name
    
    # pass the test case
    def pass_case(self):
        self.passed=True
    
    # fail the test case
    def fail_case(self):
        self.passed=False
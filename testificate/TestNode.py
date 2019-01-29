from inspect import ismethod, getframeinfo, stack
import sys
from .Case import Case, CaseType
import time

# a class defining how a test node should behave
class TestNode:

    def __init__(self,run_immediate=True):
        self.setup()
        self.run_immediate=run_immediate
        self.cases=[]
        self.case_count=0
        self.time_taken=0.0

        # start the timer to count the time of node execution
        if self.run_immediate:
            self.run_tests()

    def __str__(self):
        s=""
        s+="\nRan "+str(self.case_count)+" tests in "+str(round(self.time_taken,5))+" seconds..."
        s+="\n------------------"
        s+="\nPassed: "+str(TestNode.get_cases_passed(self))
        s+="\nFailed: "+str(TestNode.get_cases_failed(self))
        s+="\n------------------"
        for case in self.cases:
            if not case.passed:
                s+="\n"+(case.__str__())
        
        return s

    # user setup function
    # this should be overwrided in the child class
    def setup(self):
        pass

    # return all cases
    def get_cases(self):
        return self.cases

    # run all test cases
    def run_tests(self):
        start_time = time.time()
        TestNode.call_all_cases(self)
        self.time_taken=time.time() - start_time

    # function to test if two values are equal or not
    def assert_equals(self,case1,case2):
        # the number of previous functions that the test was called from
        # IMPORTANT: if the internal structure of this class is changed, this will break!
        stack_index=2
        # get the information from the stack frame about the function that called this function
        info=TestNode.get_function_call_info(stack_index)
        # create a new case
        c=Case(CaseType.EQUALS,filename=info[0],lineno=info[1],function=info[2])
   
        if case1 == case2:
            c.pass_case()

        # append the case to the node
        self.cases.append(c)
        # increase case count
        self.case_count+=1
    
    # function to test if an item contains another item (item 2 contains item 1)
    def assert_contains(self,item1,item2):
        # the number of previous functions that the test was called from
        # IMPORTANT: if the internal structure of this class is changed, this will break!
        stack_index=2
        # get the information from the stack frame about the function that called this function
        info=TestNode.get_function_call_info(stack_index)
        # create a new case
        c=Case(CaseType.CONTAINS,filename=info[0],lineno=info[1],function=info[2])

        if item1 in item2:
            c.pass_case()

        # append the case to the node
        self.cases.append(c)
        # increase case count
        self.case_count+=1




    # retrieves all information from a function call on the stackframe at a specific position
    @staticmethod
    def get_function_call_info(stack_index):
        caller = getframeinfo(stack()[stack_index][0])
        filename=caller.filename
        lineno=caller.lineno
        function=caller.function
        return (filename,lineno,function)

    # used to call all test cases in a class that extends TestNode (this)
    @staticmethod
    def call_all_cases(node, *args, **kwargs):
        for name in dir(node):
            attribute = getattr(node, name)
            if ismethod(attribute):
                # IMPORTANT: for a test to run it must have the prefix test_ in the function name
                if "test_" in attribute.__name__:
                    attribute(*args, **kwargs)

    # used to create a new test case 
    @staticmethod
    def create_case():
        return Case()

    # count how many cased have passed
    @staticmethod
    def get_cases_passed(node):
        passed=0
        for case in node.cases:
            if case.passed:
                passed+=1
        return passed

    # count how many cased have failed
    @staticmethod
    def get_cases_failed(node):
        failed=0
        for case in node.cases:
            if not case.passed:
                failed+=1
        return failed

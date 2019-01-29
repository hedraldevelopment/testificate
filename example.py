# example testing file

# from the testificate directory, import the testificate file
from testificate import testificate

# create a class that extends TestNode
class example(testificate.TestNode):

    # defining an equals test function using the "test_ prefix"
    def test_equals(self):
        self.assert_equals(1,1)

    # defining a contains test function using the "test_ prefix"
    def test_contains(self):
        self.assert_contains("1","(1,2,3)")

# instantiate a new example class
example=example()
# displaying the test node results
print(example)

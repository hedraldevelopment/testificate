from testificate import testificate

class example(testificate.TestNode):

    # defining an equals test function using the "test_ prefix"
    def test_equals(self):
        self.assert_equals(1,1)

    # defining a contains test function using the "test_ prefix"
    def test_contains(self):
        self.assert_contains("1","(1,2,3)")

example=example()
# displaying the test node results
print(example)

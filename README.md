# testificate
A lightweight Python3 testing framework!

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
Python3 +
```

### Installing

A step by step series of examples that tell you how to get a development env running

First downlad the gihub project and include the "testificate" folder in your project.
To use the framework, import the testificate file from the testificate folder

```
from testificate import testificate
```

Thats it!

## Running tests

How to get started running tests

### Types of tests ###
 There are currently 2 types of tests:
 ```
 assert_equals(item1, item2)
 ```
 and
 ```
 assert_contains(item, item_list)
 ```

### Creating a testing node

Tests are all run from within a TestNode class, specifically your own custom class than inherits from testificate.TestNode

```
class exampleTest(testificate.TestNode):
  ...
```
You can run all setup code in the setup function that will automatically be called in the constructor of TestNode
```
class exampleTest(testificate.TestNode):
  def setup(self):
   ...
```

### Definining testing functions

A testing function is a function that can run any number of tests, these must include "test_" in the name of the function.
When the class is instantiated, all these functions will automatically be called.

```
class exampleTest(testificate.TestNode):
  def test_hello(self):
    self.assert_equals(1,2)
```

If you dont want tests to run automatically, you can explicitly prevent this in the class constructor
```
example_object = exampleTest(run_immediate=False)
example_object.run_tests()
```
### Displaying the tests:
To display the tests, just print the object
```
example_object=example()
print(example_object)
```
```
Ran 1 tests in 0.011 seconds...
------------------
Passed: 0
Failed: 1
------------------
FAILED : test_hello ~ EQUALS -> testing.py at line 14
```

## Other projects

* [hedral](http://www.hedral.info/portfolio/apps) - All my other projects



## Authors

* **James Clarke** - *...Everything*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* thanks to stack overflow... couldn't have done it without you

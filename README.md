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

### Creating a testing node

Tests are all run from within a TestNode class, specifically your own custom class than inherits from testificate.TestNode

```
class exampleTest(testificate.TestNode):
  ...
```

### Definining testing functions

A testing function is a function that can run any number of tests, these must include "test_" in the name of the function.
When the class is instantiated, all these functions will automatically be called.

```
class exampleTest(testificate.TestNode):
  test_hello():
    self.assert_equals(1,2)
```

If you dont want tests to run automatically, you can explicitly prevent this in the class constructor
```
example_object = exampleTest(run_immediate=False)
example_object.run_tests()
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

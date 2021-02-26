# TEJASWI REDDY KANDULA

## SUBTOPIC: Wordcount using Flink
## Prerequisites
* Apache Flink 
* Pip
* Python(3.6.0 to 3.8.0 version)

## Installation of Python
If any other versions of python are previously installed in your system use the below command to uninstall
```
choco uninstall python
```
To install python of a specific version use the below command
```
choco install python version=3.8.0
```
## Installation steps for PyFlink

The version of python should be (3.5, 3.6, 3.7 or 3.8) for PyFlink. Please run the following command to make sure that it meets the requirements:
```
$ python --version
```
Use the below command to install apache-flink 
```
$ python -m pip install apache-flink 
```
You can also build PyFlink from source by following the development guide.

Note Starting from Flink 1.11, it’s also supported to run PyFlink jobs locally on Windows and so you could develop and debug PyFlink jobs on Windows.

### Video:
[Link to Video](https://app.vidgrid.com/view/ELbJK68EX0hP) 

## Code for wordcount using pyflink:

```
import logging
import os
import shutil
import sys
import tempfile

from flink.plan.Environment import get_environment
from flink.functions.GroupReduceFunction import GroupReduceFunction

class Adder(GroupReduceFunction):
  def reduce(self, iterator, collector):
    count, word = iterator.next()
    count += sum([x[0] for x in iterator])
    collector.collect((count, word))

env = get_environment()
data = env.from_elements("Who's there?",
 "I think I hear them. Stand, ho! Who's there?")

data \
  .flat_map(lambda x, c: [(1, word) for word in x.lower().split()]) \
  .group_by(1) \
  .reduce_group(Adder(), combinable=True) \
  .output()

env.execute(local=True)

# To read data from files

env = get_environment()
text = env.read_text("file:///path/to/file")
# Transformations to the new dataset

data.map(lambda x: x*2)

# Dataset that needs to be written to disk.Can call one of these methods on DataSet:

data.write_text("<file-path>", WriteMode=Constants.NO_OVERWRITE)
write_csv("<file-path>", line_delimiter='\n', field_delimiter=',', write_mode=Constants.NO_OVERWRITE)
output()
```
### Output: 

* I have run this code in Flink in Local Machine iam getting Module_not found error iam trying to resolve it.I will update it once it gets resolved.

### References:

* [ApacheFlinkExample](https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/batch/python.html)
* [ApacheFLink](https://flink.apache.org/)

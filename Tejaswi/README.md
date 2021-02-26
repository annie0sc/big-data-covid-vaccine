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

## Script:

![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/Wordcount.PNG)

### Output: 

![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/Output.PNG)

### References:

* [ApacheFlink](https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/batch/python.html)
* [StackOverFlow](https://stackoverflow.com/questions/63367299/how-can-you-load-a-csv-into-pyflink-as-a-streaming-table-source)

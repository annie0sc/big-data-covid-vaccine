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
[Link to Video](https://use.vg/UM7lcl) 

- Used the below command in powershell terminal to excute the python script
```
$ python column.py
```
## Code for wordcount using pyflink:

- Table API applications begin by declaring a table environment; either a BatchTableEvironment for batch applications or StreamTableEnvironment for streaming applications. This serves as the main entry point for interacting with the Flink runtime. It can be used for setting execution parameters such as restart strategy, default parallelism, etc. The table config allows setting Table API specific configurations.

```
exec_env = ExecutionEnvironment.get_execution_environment()
exec_env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(exec_env, t_config)
```
- It is used to create a TABLE as known from relational databases from a connector declaration.The connector describes the external system that stores the data of a table. Storage systems such as Apacha Kafka or a regular file system can be declared here.Below is the code to declare connector using source and sink.

- The table environment created, then declare source

```
 t_env.connect(FileSystem().path(str(root / "covid_19_clean_complete.csv")))
    .with_format(Csv())
    .with_schema(
        Schema().field("Date", DataTypes.DATE(True)).field("word", DataTypes.STRING())
    )
    .create_temporary_table("mySource")
```
- To declare sink.
```
 t_env.connect(FileSystem().path(str(out_path)))
    .with_format(Csv())
    .with_schema(
        Schema().field("word", DataTypes.STRING()).field("count", DataTypes.BIGINT())
    )
    .create_temporary_table("mySink")
```
- DDL commands to count all country cases
```
t_env.from_path("mySource")
    .group_by("word")
    .select("word, count(1) as count")
    .filter("count > 1")
    .insert_into("mySink")
 ```
 - To execute
 ```
t_env.execute("word_count2")
 ```
## Script:

![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/Wordcount.PNG)

### Output: 

1.Output dataset after executing the complete covid cases dataset.
* [Outputdataset](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/output.csv)

![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/Output.PNG)

### References:

* [ApacheFlinkExample](https://ci.apache.org/projects/flink/flink-docs-release-1.0/apis/batch/python.html)
* [Dataset taken from kaggle](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Tejaswi/covid_19_clean_complete.csv) 
* [StackOverFlow](https://stackoverflow.com/questions/63367299/how-can-you-load-a-csv-into-pyflink-as-a-streaming-table-source)
* [API](https://www.bookstack.cn/read/Flink-1.10-en/5429ac7abe3afbba.md)


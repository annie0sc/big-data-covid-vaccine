# Big Data - Covid Vaccine

## Objective

Covid-19 is currently the topic of research this season. We have decided to work on analyzing the recovery rates of patients based on their age, gender, and other criteria. To achieve this, we will be using a dataset from Kaggle to process static data, then we will move to live streaming data from Twitter. Apache Hadoop will be used as the file system, Apache Flink will be used for live streaming data from Twitter and Python will be tying together this whole project, hence the name: PyFlink-Covid-Vaccine.

## Meet the Team

<table>
<td align="center"><a href="https://github.com/SwaroopReddyGottigundala"><img src="https://avatars.githubusercontent.com/u/60024334?s=460&u=20ef224b43a8e817fdceb9e558d631e1a6e7435d&v=4" width="100px;" alt=""/><br /><sub><b>Swaroop Reddy</b></sub></a><br /></td>

<td align="center"><a href="https://github.com/annie0sc"><img src="https://avatars.githubusercontent.com/u/28427324?s=460&u=31b810c008419d5bfb81c152d51ec90cb96dc28b&v=4" width="100px;" alt=""/><br /><sub><b>Annie Chandolu</b></sub></a><br /></td>

<td align="center"><a href="https://github.com/alekhyajaddu"><img src="https://avatars.githubusercontent.com/u/60018848?s=460&u=7cc6d01354b7857d88890a77b510232333fb9b53&v=4" width="100px;" alt=""/><br /><sub><b>Alekhya Jaddu</b></sub></a><br /></td>

<td align="center"><a href="https://github.com/Teju2404"><img src="https://avatars.githubusercontent.com/u/60014237?s=460&u=f01438bd5720ded87bb9f744c26a9e706853c0a2&v=4" width="100px;" alt=""/><br /><sub><b>Tejaswi Reddy Kandula</b></sub></a><br /></td>

<td align="center"><a href="https://github.com/anshithavelagapudi"><img src="https://avatars.githubusercontent.com/u/60020144?s=460&v=4" width="100px;" alt=""/><br /><sub><b>Naga Anshitha Velagapudi</b></sub></a><br /></td>

<td align="center"><a href="https://github.com/KHARIKA17"><img src="https://avatars.githubusercontent.com/u/60010885?s=460&u=24c5428d5a37b37a3efd752d271740b402177734&v=4" width="100px;" alt=""/><br /><sub><b>Harika Kulkarni</b></sub></a><br /></td>

</table>

## Datasets Used

### Static Dataset: 
* [covid-metrics](https://www.kaggle.com/imdevskp/corona-virus-report?select=country_wise_latest.csv)

### Streaming Data:
* We will be using live streaming data, tweets, from Twitter as part of our future improvements to the project.

## Tech Stack

* Progamming Language: [Python](https://docs.python.org/3/c-api/index.html)
* Steaming Engine: [Flink](https://flink.apache.org/)
* [Wiki-Link for Flink](https://github.com/apache/flink)
* File System: [Hadoop](https://hadoop.apache.org/docs/stable/api/index.html)

## Tasks/Issues
* Swaroop Reddy - Going to work on HDFS (Hadoop) MapReduce Programming Model.
* Annie Samarpitha - I will be working with Alekhya on Python programming. 
* Alekhya Jaddu - Will be working on the programming part using Python scripts.
* Tejaswi Reddy Kandula - Going to work on Shell Scripting. 
* Naga Anshitha Velagapudi - Going to work on Flink which is used to process data streams in large data.
* Harika Kulkarni - Will be working on Flink.

## SubTopics:
1. Swaroop Reddy Gottigundala- Datastream Processing.
1. Annie Samarpitha Chandolu- Analysis on weekly-cases and deaths-weekly counts.
1. Alekhya Jaddu - Wordcount using pyFlink.
1. Tejaswi Reddy Kandula - Wordcount using Flink
1. Naga Anshitha Velagapudi - Analyze active and critical cases.
1. Harika Kulkarni - countrywise highest recovery rates versus death rates.

## Prerequisites
* Apache Flink 
* Pip
* Python(3.6.0 to 3.8.0 version)

## Description
## Apache Flink
- Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.
- Flink also provides batch processing, graph processing, Itearative proccessing for Machine learning applications.
- Flink is considered as the next-gen stream processing system.
- Flink offers substantially higher processing speeds to spark and hadoop.
- Flink provides low latency and high throughput

## ALEKHYA JADDU
## Sub-Topic: WordCount using pyFlink
### Prerequisites:
* Apache Flink 
* PIP
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

### Code for Word Count using PyFlink:
[word_count.py](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Alekhya/word_count.py)
### Input file
[input.txt](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Alekhya/covid19-INDIA.txt) 
### Output file
[output.txt](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Alekhya/output.txt)

### Demonstration video
https://app.vidgrid.com/view/zGuTOAcK3IiC

 ## Annie Chandolu

 ### Subtopic: *Analysis on weekly-cases and deaths-weekly counts*

 I am doing an analysis on a Covid dataset which is stored in the following repository:

 https://github.com/annie0sc/practice-flink-wordcount

 #### A Preview of my work: VIDEO

 https://use.vg/hboCoj

## Harika Kulkarni

### Subtopic:Countrywise highest recovery rates versus death rates

I am working on providing Countrywise highest recovery rate versus death rates on Covid data.

Pre-requites:
1.Python
2.Flink
3.pip


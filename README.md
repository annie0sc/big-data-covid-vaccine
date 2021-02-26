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
1. Swaroop Reddy Gottigundala- Writing a Flink python datastream API program.
1. Annie Samarpitha Chandolu- Analysis on weekly-cases and deaths-weekly counts.
1. Alekhya Jaddu - Wordcount using pyFlink.
1. Tejaswi Reddy Kandula - Wordcount for all covidcases using pyFlink for the dataset [covid_19_clean_complete](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/datasets/covid_19_clean_complete.csv)
1. Naga Anshitha Velagapudi - Analyzing number of times/days the country had taken vaccinations.
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
choco install python --version=3.8.0
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

#### Prerequisites:
- Python
- Flink
- pip

### Google Colab:
Colab is a Python development environment that runs in the browser using Google Cloud.
We can perform the following using Google Colab.
- Write and execute code in Python
- Document your code that supports mathematical equations
- Create/Upload/Share notebooks
- Import/Save notebooks from/to Google Drive
- Import/Publish notebooks from GitHub
- Import external datasets e.g. from Kaggle
- Integrate PyTorch, TensorFlow, Keras, OpenCV
- Free Cloud service with free GPU

#### Steps for Using Google colab:
  Input File: [Link to input file](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/datasets/worldometer_data.csv)
- Step1: As Colab implicitly uses Google Drive for storing your notebooks, ensure that you are logged in to your Google Drive account before proceeding further.

- Step2: Open the following URL in your browser: https://colab.research.google.com
Your browser would display the following screen (assuming that you are logged into your Google Drive):
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/first%20screen.JPG)

- Step3: Click on the NEW NOTEBOOK link at the bottom of the screen. A new notebook would open up as shown in the screen below.
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/second%20screen.JPG)

- Step4: You will now enter a trivial Python code in the code window and execute it.Enter the following two Python statements in the code window and click on the arrow on the left side of the code window.
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/third%20screen%20new.png)

- Step5: Install apache-flink and all necessary packages using below command.
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/apache%20flink%20installation.JPG)

- Step6: Reading the data from Input file.
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Reading%20the%20data%20from%20input%20file.JPG)

- Step7: Comparing between TotalDeaths and TotalRecovered from Covid data.
![](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/bar%20graph%20showing%20the%20deaths%20vs%20recovered.JPG)

 Output File:[Link to Output file](https://github.com/KHARIKA17/bigdata_group4_harika/blob/main/Bigdata_assg.ipynb)
 
 References:[https://flink.apache.org/flink-architecture.html](https://flink.apache.org/flink-architecture.html)
### Demonstration Video Link: [Video Link](https://app.vidgrid.com/view/mQgPtWuJlcEU)

# Naga Anshitha velagapudi

## Subtopic: 
I'm working on analyzing number of times/days a country had taken vaccinations.

[Demonstration Video](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Anshitha/Video.mp4)

### My Repo: 
[Link](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Anshitha/README.md)

### Dataset:
[Link](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/datasets/vaccinations.csv)

### Input:
[Link](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Anshitha/word_count_vaccine.py)

### Output:
[Link](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Anshitha/output_vaccines.csv)

### References:
1. [Description](https://www.alibabacloud.com/blog/the-flink-ecosystem-a-quick-start-to-pyflink_596150)
2. [Kaggle_Dataset](https://www.kaggle.com/schandra005/covid-19-vaccination)
3. [Code_Reference](https://stackoverflow.com/questions/63367299/how-can-you-load-a-csv-into-pyflink-as-a-streaming-table-source)

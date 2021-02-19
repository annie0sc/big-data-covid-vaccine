## Naga Anshitha Velagapudi
[Video](https://github.com/annie0sc/big-data-covid-vaccine/blob/main/Anshitha/zoom_0.mp4)

# Flink
[Flink-python](https://github.com/apache/flink/tree/master/flink-python)

Apache Flink is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams. Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.

## The Flink Ecosystem: A Quick Start to PyFlink

- PyFlink is simply a combination of Apache Flink with Python, or rather Flink on Python.
- First, the combination of the two means that you can use all of Flink's features in Python.
- PyFlink also allows you to use the computing capabilities of Python's extensive ecosystem on Flink, which can in turn help further facilitate the development of its ecosystem

## Why Flink and Python?

To understand why, let's first consider some of the benefits of using the Flink framework:

- Advantageous architecture: Flink is a pure stream computing engine with unified stream and batch processing capabilities.
- Fresh vitality: Flink is the most active open-source project in 2019 according to objective statistics of ASF.
- High reliability: As an open-source project, Flink has long been tested and widely applied in big data companies' production environments.

## The PyFlink Architecture

- Make all Flink features available to Python users.
- Run Python's analysis and computing functions on Flink to improve Python's ability to resolve big data issues.

### The Key Issue

- Establish a handshake between a Python virtual machine (PyVM) and a Java virtual machine (JVM), which is essential for Flink to support multiple languages.
- To resolve this issue, we must select an appropriate communications technology.
- They are Apache Beam and Py4J.

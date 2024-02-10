# End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera



<!-- TABLE OF CONTENTS -->
## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#SystemArchitecture)
- [Tool Used :](#ToolUsed )
- [get started](#getstarted)
- [License](#license)
<!-- END OF TABLE OF CONTENTS -->




<a name="introduction"></a>
## Introduction
This project focuses on building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper,pandas and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.

<a name="SystemArchitecture"></a>
## SystemArchitecture
![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/Image1.png)



<a name="ToolUsed "></a>
## Tool Used


- **Data Source:** We use randomuser.me API to generate random user data for our pipeline.
- **Apache Airflow:** Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper:** Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry:** Helps in monitoring and schema management of our Kafka streams.
- **Cassandra:** Where the processed data will be stored.
- **Pandas:** for Cleaning,preprocessing ,Manipulating and transforming data

<a name="getstarted"></a>
## get started

## Get Started
Follow these steps to get started with the project:
1. **activte the virtual envairement**
    ```sh
     .\myenv\Scripts\Activate   
2. **Clone the repository:**
   ```sh
   git clone https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera.git
3. **Go to the project folder**
 ```sh
   cd myenv
4. **Build the environment with Docker Compose:**
 ```sh
   docker-compose up
 ```



<a name="license"></a>
## License
...






This project focuses on extracting data from random users api "https://randomuser.me/api/"
 
 
 
 how I built a simple end-to-end data engineering project using Docker, Apache Airflow, Kafka, Spark, Cassandra, PostgreSQL,

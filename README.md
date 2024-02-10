# End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera



<!-- TABLE OF CONTENTS -->
## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#SystemArchitecture)
- [Tool Used :](#ToolUsed )
- [get started](#getstarted)
- [Results](#license)
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


## Get Started
This project focuses on extracting data from random users api "https://randomuser.me/api/"
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
```
4. **create image**
 ```sh
   docker build -t pandas-image -f Dockerfile.pandas . 
 ```
5. **Build the environment with Docker Compose:**
```sh
   docker-compose up
 ```
And you will get this :
![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image%205.png)

### with
- **Kafka Broker:** Part of the Kafka streaming system, it manages message storage, access, and transport.
- **Zookeeper:** A service for distributed setup and coordination, essential for Kafka’s distributed functioning.
- **Schema Registry:** Offers a REST interface to store and fetch Avro schemas, aiding Kafka streams in recognizing record schemas.
- **Control Center**: A web tool for overseeing Kafka setups, allowing data checks, topic generation, and Kafka Connect configuration.
- **Cassandra DB:** A NoSQL database suitable for large-scale, high-speed data spread across multiple nodes, ensuring no sole point of breakdown. Used here so as to load the processed data.
- **PostgresDB:** A relational database employed as Apache Airflow’s metadata storage and also as a versatile data repository.
ETL Service: After dockerizing the pipeline scripts, added the service to Compose for us to automatically update, build, and push the Docker image to DockerHub with GitHub Actions’ CI script.
- **Airflow Webserver:**Airflow’s UI for outlining and overseeing data workflows or DAGs.
- **Scheduler:** Within Airflow, it kickstarts tasks and forms data pipelines, ensuring timely execution or activation by other tasks.
- **End-of-Project Container:** This container is responsible for running our final script, `ali.py`, which exists in the `myenv` directory. Additionally, it consumes messages from our topic named `users_created` and loads our data into the `cassandra_db`.




<a name="license"></a>
## Results
#### Streamlining Data to Apache Kafka

After getting your Docker containers active, initiate a new Airflow DAG. Then, navigate to the Airflow interface at http://localhost:8084/home?status=active and execute the user_automation DAG by clicking the play icon in the actions section.
![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image%203.png)


 ####  And, to observe the live data stream, access the control center interface at localhost:9021.
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image15.png)
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image8.png)
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image9.png)
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image10.png)
    
#### Streaming Data into Cassandra

 ###### by Establish then a connection to the cluster to see the data stored in Cassandra.
 - Keyspaces and their tables should display accordingly when running:
  ```sh
cqlsh
 ```
  ```sql
DESCRIBE spark_streams.created_users;
 ```
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image%201.png)
 
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/image%202.png)



- To retrieve the data transferred to Cassandra, eecute:
  
  ```sql
  SELECT * FROM spark_streams.created_users;
   ```
  
 
 ![Screenshot](https://github.com/2000aliali/End-End-data-engineering-Project-streaming-from-random-users-API-to-cassandera/blob/master/images/iamge%204.png)
 
 


 
 
 


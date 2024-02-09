import uuid
import json
import time
import logging
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests

default_args = {
    'owner': 'airscholar',
    'start_date':  datetime.now(),
}

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]
    return res

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():

    from kafka import KafkaProducer

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time=time.time()
    #producer.send('users_created', json.dumps(formatted_data).encode('utf-8'))



    while True:
        if time.time() > curr_time + 60: 
          
           break
        try:


            res = get_data()
            print("getting datta using request")
            formatted_data = format_data(res)
            print("formating data ***************")
            producer.send('users_created', json.dumps(formatted_data).encode('utf-8'))
        except Exception as e:

            logging.error(f'An error occurred: {e}')

            continue




with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data,
    )

#stream_data();
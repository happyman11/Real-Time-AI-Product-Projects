import numpy as np
from flask import Flask, request, jsonify

import requests
import json
import os

url='http://127.0.0.1:5000/course_recommendation'

data = {'Course Name': 'Rust up and Running'}
data = json.dumps(data)
send_requests=requests.post(url,data)
print(send_requests)
result=send_requests.json()

for i in result:
    print("Recommended_Course : ", i)
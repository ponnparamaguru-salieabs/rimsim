import json
from datetime import datetime
import random
import time
import paho.mqtt.client as mqtt 

base_data = {}
count = 0

# can_ids = ["CC10010001", "CC10010002", "CC10010003", "CC10010004", "CC10010005"]
can_ids = ["CC10010001"]

broker_address = "104.237.2.25"  
broker_port = 1883  
client = mqtt.Client("PublisherClient")  
client.connect(broker_address, broker_port, 60)

for i in range(1, 101):
    for i in range(1, 3):
        device_id = f"POC10{i:02d}"
        for j in range(1, 2):
            position_id = f"POC10{i:02d}{j:03d}"
            device_info = base_data.copy()
            device_info["deviceId"] = device_id
            device_info["positionID"] = position_id
            device_info["canID"] = random.choice(can_ids)  
            device_info["canResult"] = "NewCan"
            device_info["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            device_info["rssi"] = "45%"

            json_output = json.dumps(device_info, indent=4)
            
            topic = f"{device_id}_OUT"
            client.publish(topic, json_output)

            with open('test3', 'a') as file:  
                file.write(f"Topic: {topic}, Message: {json_output}\n")
            
            print(f"Published to topic {topic}: {json_output}")
            # time.sleep(0.2)
            count += 1
            print(f"count: {count}")
            print()
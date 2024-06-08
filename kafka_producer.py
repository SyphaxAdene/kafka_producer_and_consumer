from confluent_kafka import Producer
import json

# Kafka configuration
conf = {
    'bootstrap.servers': 'SASL_SSL://pkc-4nmjv.francecentral.azure.confluent.cloud:9092',
    'sasl.mechanisms': 'PLAIN',
    'security.protocol': 'SASL_SSL',
    'sasl.username': 'ZV4GHSLDIHI554G4',
    'sasl.password': 'CubYOqIlQCX1A/hFRfDa0Ay87GciTQ93+0dZTmgz1r/XFwLNjfg2rB2RL7GzsRli'
}

# Create Producer instance
producer = Producer(conf)

# Callback when message is delivered or failed
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# JSON message
message = {
    "stationId": "PS123",
    "name": "Downtown Parking Station",
    "location": {
        "address": "123 Main St, Downtown, CityName",
        "latitude": 40.712776,
        "longitude": -74.005974
    },
    "capacity": {
        "totalSpots": 150,
        "availableSpots": 75
    },
    "rates": {
        "hourlyRate": 2.50,
        "dailyRate": 20.00,
        "monthlyRate": 150.00
    },
    "operatingHours": {
        "monday": {
            "open": "08:00",
            "close": "22:00"
        },
        "tuesday": {
            "open": "08:00",
            "close": "22:00"
        },
        "wednesday": {
            "open": "08:00",
            "close": "22:00"
        },
        "thursday": {
            "open": "08:00",
            "close": "22:00"
        },
        "friday": {
            "open": "08:00",
            "close": "22:00"
        },
        "saturday": {
            "open": "10:00",
            "close": "20:00"
        },
        "sunday": {
            "open": "10:00",
            "close": "18:00"
        }
    },
    "amenities": {
        "hasEVCharging": True,
        "hasHandicapAccess": True,
        "hasSecurityCameras": True,
        "acceptsCreditCard": True
    },
    "contactInfo": {
        "phone": "+1-234-567-890",
        "email": "contact@downtownparking.com"
    },
    "lastUpdated": "2024-06-07T10:15:30Z"
}

# Produce the message
producer.produce('iot_data_topic', key="01", value=json.dumps(message), callback=delivery_report)
producer.poll(0)

# Wait for any outstanding messages to be delivered
producer.flush()

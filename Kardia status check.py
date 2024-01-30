from twilio.rest import Client
import requests
import time

# Replace with your Twilio credentials and phone numbers
TWILIO_ACCOUNT_SID = 'kkkkkkkkkkkkkkkkk'
TWILIO_AUTH_TOKEN = '999999999999999999'
TWILIO_PHONE_NUMBER = '+0193994003'
RECIPIENT_PHONE_NUMBER = '+842492949022230020020020020020'

# Replace with the desired city (Delhi) coordinates
DELHI_LATITUDE = '28.6139'
DELHI_LONGITUDE = '77.2090'

# Function to check for earthquakes in Delhi
def check_earthquakes():
    base_url = 'https://earthquake.usgs.gov/fdsnws/event/1/query'
    params = {
        'format': 'geojson',
        'latitude': DELHI_LATITUDE,
        'longitude': DELHI_LONGITUDE,
        'maxradiuskm': 50,  # Adjust the radius as needed
        'minmagnitude': 4.0  # Adjust the magnitude threshold as needed
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if data['features']:
        send_continuous_alerts(f"Red color at Kardia !!!")

# Function to send a WhatsApp message using Twilio
def send_whatsapp_message(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_='whatsapp:' + TWILIO_PHONE_NUMBER,
        body=message,
        to='whatsapp:' + RECIPIENT_PHONE_NUMBER
    )
    print(f"WhatsApp message sent. SID: {message.sid}")

# Function to send continuous alerts for a specified duration
def send_continuous_alerts(message, duration_minutes=10):
    end_time = time.time() + duration_minutes * 60
    while time.time() < end_time:
        send_whatsapp_message(message)
        time.sleep(180)  # Sleep for 3 minutes between alerts

# Main loop to run the script continuously
while True:
    check_earthquakes()
    time.sleep(180)  # Sleep for 3 minutes before checking again

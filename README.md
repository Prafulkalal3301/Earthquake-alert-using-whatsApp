Code Overview:
Our Python script combines the power of Twilio for messaging and the USGS Earthquake API to keep an eye on seismic activities around Delhi. Here's a quick breakdown:

A: Twilio Setup:

  @@@Replace the placeholders (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, and RECIPIENT_PHONE_NUMBER) with your personal Twilio details.
B: Earthquake Check:
  @@@The script talks to the USGS Earthquake API, looking for quakes within a certain radius of Delhi and with a magnitude greater than 4.0.
C: Alert Function:
  @@@When an earthquake is detected, the script becomes your digital superhero, sending out WhatsApp alerts for a set duration (default is 10 minutes).

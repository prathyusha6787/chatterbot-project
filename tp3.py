import smtplib
import requests

# Function to send an email notification
def send_email(subject, body):
    # Set up the email server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("your_email@gmail.com", "your_password")

    # Set up the email message
    msg = "Subject: {}\n\n{}".format(subject, body)

    # Send the email
    server.sendmail("your_email@gmail.com", "recipient_email@gmail.com", msg)
    server.quit()

# Function to check for earthquakes
def check_earthquakes():
    # Get the latest earthquake data from the USGS API
    response = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson")
    data = response.json()

    # Check if there are any earthquakes with a magnitude of 5.0 or greater
    for feature in data["features"]:
        mag = feature["properties"]["mag"]
        if mag >= 5.0:
            # If there is an earthquake, send an email notification
            subject = "Earthquake Alert: Magnitude {}".format(mag)
            body = "An earthquake with a magnitude of {} has occurred. Check the USGS website for more information.".format(mag)
            send_email(subject, body)

# Check for earthquakes every 10 minutes
while True:
    check_earthquakes()
    time.sleep(600) # wait 10 minutes

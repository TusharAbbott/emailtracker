from flask import Flask, send_file, request
from datetime import datetime

app = Flask(__name__)

logFile = 'log.txt'
your_ip = ''

@app.route('/')
def index():
  image_path = 'test.webp'

  # Set the MIME type of the image
  mimetype = 'image/jpeg'
  ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)

  # Get the current date and time
  current_datetime = datetime.now()

  # Convert the datetime object to a string
  formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

  if (ip_address != your_ip):
    with open('log.txt', "a") as f:
      f.write("Email opened at: " + str(formatted_datetime) + " IP: " +
              str(ip_address) + "\n")
  # Return the image as a response
  return send_file(image_path, mimetype=mimetype)


@app.route('/count')
def count_lines():
  line_count = 0
  try:
    with open(logFile, 'r') as file:
      for line in file:
        line_count += 1
    return f"Email opened {line_count} times"
  except FileNotFoundError:
    return "Error"


app.run(host='0.0.0.0', port=81)

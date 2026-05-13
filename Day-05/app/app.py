from flask import Flask
import redis
import socket

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis_client.incr('visits')
    visits = redis_client.get('visits').decode('utf-8')

    hostname = socket.gethostname()

    return f"""
<h1>Flask Application Running Successfully</h1>

<p>Served by container: <strong>{hostname}</strong></p>

<p>Total Visits: <strong>{visits}</strong></p>

<p>Powered by Docker Compose, NGINX, and Redis</p>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

# Runs a test server
from app import app
app.run(host='192.168.56.10', port=8080, debug=True)

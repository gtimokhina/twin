# magnum is used to handle the lambda function
from mangum import Mangum
from server import app
# server.py is the file that contains the FastAPI app

# Create the Lambda handler
handler = Mangum(app)
from dotenv import load_dotenv
import os
load_dotenv()

auth0_domain = os.environ.get('AUTH0_DOMAIN')
api_audience = os.environ.get('API_AUDIENCE')

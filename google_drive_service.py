from Google import Create_Service

CLIENT_SECRET_FILE = 'token.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

DOCX_MIME_TYPE = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

drive_service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

"""Load environmental variables into configuration."""
import os

from dotenv import load_dotenv
load_dotenv()

database = {
    "driver": str(os.getenv("DB_DRIVER")),
    "server": str(os.getenv("DB_SERVER")),
    "name": str(os.getenv("DB_NAME")),
    "uid": str(os.getenv("DB_UID")),
    "pwd": str(os.getenv("DB_PWD")),
    "encrypt": str(os.getenv("DB_ENCRYPT")),
    "trustServerCert": str(os.getenv("DB_TRUST_SERVER_CERT")),
    "hostNameInCert": str(os.getenv("DB_HOST_NAME_IN_CERT")),
    "loginTimeout": os.getenv("DB_LOGIN_TIMEOUT")
}
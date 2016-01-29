import logging
import os

environment = os.environ.get('Environment', 'dev')

output_file = os.environ.get(
    'LOGGING_SERVICE_OUTPUT_FILE', '/var/log/logging-service.log')

app_name = os.environ.get(
    'LOGGING_SERVICE_APP_NAME', 'logging-service')

logging_service_name = os.environ.get(
    'LOGGING_SERVICE_LOGGER_NAME', 'logging-service')

host = os.environ.get(
    'LOGGING_SERVICE_HOST', 'http://127.0.0.1')
port = os.environ.get(
    'LOGGING_SERVICE_PORT', '5000')

logging_levels = {
    "NOTSET": logging.NOTSET,
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL
}

loggly_uri = os.environ.get(
    'LOGGING_SERVICE_LOGGLY_URI',
    'https://logs-01.loggly.com/inputs/77c54e3f-33b7-4f8b-a2a7-dbaef3414348/tag/python')

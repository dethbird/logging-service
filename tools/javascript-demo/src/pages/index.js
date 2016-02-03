var LoggingServiceClient = require('../lib/LoggingServiceClient');

var logger = new LoggingServiceClient({"baseUrl": "http://11dd6794.ngrok.io"});

logger.syslog("DEBUG", "Something happened", {"foo": "bar"});
logger.page({"foo": "bar"});

$('a.btn').on('click', function(){
  logger.event("Analytics Overview", "Click Calendar", $(this).html(), $(this).html().replace(" Month", ""), {
    "foo": "bar"
  });
});

"use strict";
class LoggingServiceClient {
  constructor(options) {
    this.baseUrl = options.baseUrl;
  }

  extendData(data) {

    data = $.extend(data,
    {
      clientInformation: {
        userAgent: window.clientInformation.userAgent,
        language: window.clientInformation.language
      },
      location: {
        href: window.location.href,
        hash: window.location.hash,
        search: window.location.search,
        port: window.location.port,
        pathname: window.location.pathname,
        protocol: window.location.protocol
      }
    });
    return data;
  }

  syslog(level, message, context) {

    var data = {
      log_level: level,
      message: message,
      context: context
    };

    data = this.extendData(data);

    $.ajax(this.baseUrl + '/syslog?log_level=' + data.log_level,
      {
        data: JSON.stringify(data),
        processData: false,
        contentType: 'application/json; charset=utf-8',
        method: 'POST',
        success: function(data){
          console.log(data);
        }
      }
    );
  }

  page(context) {

    var data = {
      context: context
    };

    data = this.extendData(data);

    $.ajax(this.baseUrl + '/page',
      {
        data: JSON.stringify(data),
        processData: false,
        contentType: 'application/json; charset=utf-8',
        method: 'POST',
        success: function(data){
          console.log(data);
        }
      }
    );
  }

  event(category, action, label, value, context) {

    var data = {
      event: {
        category: category,
        action: action,
        label: label,
        value
      },
      context: context
    };

    data = this.extendData(data);

    $.ajax(this.baseUrl + '/event',
      {
        data: JSON.stringify(data),
        processData: false,
        contentType: 'application/json; charset=utf-8',
        method: 'POST',
        success: function(data){
          console.log(data);
        }
      }
    );
  }


}
module.exports = LoggingServiceClient;

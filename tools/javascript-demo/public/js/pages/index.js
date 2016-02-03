(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
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

},{}],2:[function(require,module,exports){
var LoggingServiceClient = require('../lib/LoggingServiceClient');

var logger = new LoggingServiceClient({"baseUrl": "http://11dd6794.ngrok.io"});

logger.syslog("DEBUG", "Something happened", {"foo": "bar"});
logger.page({"foo": "bar"});

$('a.btn').on('click', function(){
  logger.event("Analytics Overview", "Click Calendar", $(this).html(), $(this).html().replace(" Month", ""), {
    "foo": "bar"
  });
});

},{"../lib/LoggingServiceClient":1}]},{},[2]);

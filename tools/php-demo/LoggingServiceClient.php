<?php
use Requests;

class LoggingServiceClient {

    private $baseUrl;

    public function __construct($baseUrl){
        $this->baseUrl = $baseUrl;
    }

    private function extendData($data) {

        $mockServerData = json_decode('{"PATH":"\/usr\/local\/bin:\/usr\/bin:\/bin","REDIRECT_STATUS":"200","PP_CUSTOM_PHP_INI":"\/var\/www\/vhosts\/dev.dethbird.com\/etc\/php.ini","HTTP_HOST":"dev.dethbird.com","HTTP_CONNECTION":"keep-alive","HTTP_CACHE_CONTROL":"max-age=0","HTTP_ACCEPT":"text\/html,application\/xhtml+xml,application\/xml;q=0.9,image\/webp,*\/*;q=0.8","HTTP_UPGRADE_INSECURE_REQUESTS":"1","HTTP_USER_AGENT":"Mozilla\/5.0 (Windows NT 10.0; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/48.0.2564.97 Safari\/537.36","HTTP_ACCEPT_ENCODING":"gzip, deflate, sdch","HTTP_ACCEPT_LANGUAGE":"en-US,en;q=0.8","HTTP_COOKIE":"PHPSESSID=k8gjn8hk02fgd29d45uj78ggr3; AWSELB=69D1EFD902FE5ECDDAABD04577FCE89C8598CC389BA356FE1674DCA03DCE424F702F1BF4EFF7111C259D083C6F27350EDFFFE59824BDF8D6D2BA47AF2FBA66CD62214963A7; _gat=1; _ga=GA1.2.153607366.1440546479","SERVER_SOFTWARE":"Apache","SERVER_NAME":"dev.dethbird.com","SERVER_ADDR":"168.144.251.114","SERVER_PORT":"80","REMOTE_ADDR":"66.108.179.56","DOCUMENT_ROOT":"\/var\/www\/vhosts\/dethbird.com\/subdomains\/dev.dethbird.com\/public","SERVER_ADMIN":"rishi.satsangi@gmail.com","SCRIPT_FILENAME":"\/var\/www\/vhosts\/dethbird.com\/subdomains\/dev.dethbird.com\/public\/index.php","REMOTE_PORT":"55843","REDIRECT_URL":"\/index.php","GATEWAY_INTERFACE":"CGI\/1.1","SERVER_PROTOCOL":"HTTP\/1.1","REQUEST_METHOD":"GET","QUERY_STRING":"","REQUEST_URI":"\/note\/test","SCRIPT_NAME":"\/index.php","ORIG_SCRIPT_FILENAME":"\/var\/www\/cgi-bin\/cgi_wrapper\/cgi_wrapper","ORIG_PATH_INFO":"\/index.php","ORIG_PATH_TRANSLATED":"\/var\/www\/vhosts\/dethbird.com\/subdomains\/dev.dethbird.com\/public\/index.php","ORIG_SCRIPT_NAME":"\/phppath\/cgi_wrapper","PHP_SELF":"\/index.php","REQUEST_TIME":1454544790}', true);

        $data['server'] = array(
            "server_name"=>$mockServerData['SERVER_NAME'],
            "phpsessid"=>$mockServerData['PHPSESSID'],
            "http_host"=>$mockServerData['HTTP_HOST'],
            "request_uri"=>$mockServerData['REQUEST_URI'],
            "query_string"=>$mockServerData['QUERY_STRING'],
            "request_method"=>$mockServerData['REQUEST_METHOD']
        );
        return $data;
    }

    public function syslog($log_level, $message, $context)
    {
        $data = array(
          "log_level" => $log_level,
          "message" => $message,
          "context" => $context
        );
        $data = $this->extendData($data);

        $response = Requests::post(
          $this->baseUrl . "/syslog?log_level=" . $log_level,
          array("Content-Type"=>"application/json"),
          json_encode($data)
        );

        return $response;
    }

}

"#!/bin/bash -ex\n"
"touch /tmp/userdata_started\n"
"yum -y update\n"
"yum -y install httpd php mysql php-mysql\n"
"chkconfig httpd on"
"/etc/init.d/httpd start\n"
"if [ ! -f /var/www/html/lab2-app.tar.gz ]; then\n"
"cd /var/www/html\n"
"wget https://s3-us-west-2.amazonaws.com/us-west-2-aws-staging/awsu-ilt/academy-cca/v3.0/labs/lab5-rds/scripts/lab5-app.tar.gz\n" 
"chown apache:root /var/www/html/rds.conf.php\n"
"fi\n" 


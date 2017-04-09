#!/bin/bash -ex
yum -y update 
yum -y install httpd php mysql php-mysql
chkconfig httpd on 
/etc/init.d/httpd start
if [ ! -f /var/www/html/lab2-app.tar.gz ]; then 
    cd /var/www/html 
    wget https://s3-us-west-2.amazonaws.com/us-west-2-aws-staging/awsu-ilt/academy-cca/v3.0/labs/lab5-rds/scripts/lab5-app.tar.gz
    gunzip lab5-app.tar.gz 
    tar -xvf lab5-app.tar
    chown apache:root /var/www/html/rds.conf.php 
fi
     

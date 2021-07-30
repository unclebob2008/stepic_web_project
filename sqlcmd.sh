sudo mysql -uroot -e "create database djangodb;"
sudo mysql -uroot -e "CREATE USER 'djuser'@'%' IDENTIFIED BY '1234';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON djangodb.* TO 'djuser'@'%';"

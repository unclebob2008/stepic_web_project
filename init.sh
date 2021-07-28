sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo rm /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart

cd /home/box/web
gunicorn --bind='0.0.0.0:8080' hello:app

cd /home/box/web/ask
gunicorn --bind='0.0.0.0:8000' ask.wsgi

#sudo /etc/init.d/mysql start

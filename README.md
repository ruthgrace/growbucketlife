# Grow Bucket Life

To renew your SSL cert:

```
sudo certbot renew
```

to make a new cert

```
certbot certonly --force-renewal -a webroot -w /var/www/growbucket -d www.growbucket.life -w /var/www/growbucket -d growbucket.life
```

to make sure nginx is reloaded after certs are renewed: https://www.guyrutenberg.com/2017/01/01/lets-encrypt-reload-nginx-after-renewing-certificates/

If you are setting this up again on another computer, symlink the nginx config to /etc/nginx/sites-available and /etc/nginx/sites-enabled, and symlink the sysctl .service config to /etc/systemd/system/. Make sure that the www-data user is in the right groups to be able to make the socket file in the directory pulled from git.

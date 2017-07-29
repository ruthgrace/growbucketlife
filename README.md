# Grow Bucket Life

Dear Ruth, next time you need to renew your SSL cert for https, go to your nginx config and comment out the part redirecting all http to https, and then run

```
certbot certonly --force-renewal -a webroot -w /var/www/html -d www.growbucket.life -w /var/www/html -d growbucket.life
```

Don't forget to redirect http to https again.

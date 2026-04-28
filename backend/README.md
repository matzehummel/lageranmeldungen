# Backend setup

## Install dependencies
```
cd backend
pip install -r requirements.txt
```

## Create .env file with following content:
```
MONGODB_CONNECTION_STRING=mongodb+srv://simba:<password>@mhcluster.hg1tjoa.mongodb.net/?retryWrites=true&w=majority
EMAIL_PASSWORD=<mail-password>
WKHTMLTOPDF_PATH=C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe
```

## Run backend in development mode
```
python app.py
```

# Prepare backend for production

## Build Docker image
Navigate to `backend` folder
Run following command
```
docker build -t lageranmeldungen_backend .
```

## Run docker image
```
docker run -p 5000:5000 lageranmeldungen_backend
```

# Setup VPS Server

## Setup DNS
- in SCP: Go to Network, under IPv4 add the domain in the rDNS column
- in CCP: Go to the corresponding domain (zeltlager-braeunlingen.de). Add an entry of type A with the corresponding IP address of the VPS in the row of the subdomain

## Add user
```
adduser <username>
usermod -aG sudo <username>
su <username>
```

## Clone repository
```
cd /var
mkdir www
cd www
sudo git clone https://github.com/matzehummel/lageranmeldungen.git
```

## Create venv
But first make sure, that python and pip are installed
```
cd lageranmeldungen/backend
sudo python3 -m venv .venv
source .venv/bin/activate
sudo chown -R $(whoami):$(whoami)  .venv/   # change owner of .venv folder
pip install -r requirements.txt
```

## setup pdf directory
We also need the pdf directory for the generated pdfs
```
mkdir -p /var/www/lageranmeldungen/backend/pdf
```
To enable gunicorn to write in this directory:

Change ownership of pdf directory (and everything inside it `-R`)
```
chown -R matze:www-data /var/www/lageranmeldungen/backend/pdf
```

Give read write and execute permissions to owner (matze) and group (www-data)
```
chmod 775 /var/www/lageranmeldungen/backend/pdf
```


## Gunicorn for WSGI
create service file
```
sudo nano /etc/systemd/system/lageranmeldungen-backend.service

[Unit]
Description=A Gunicorn WSGI for Lagernameldungen Backend
After=network.target
[Service]
User=matze
Group=www-data
WorkingDirectory=/var/www/lageranmeldungen/backend
Environment="PATH=/var/www/lageranmeldungen/backend/.venv/bin"
ExecStart=/var/www/lageranmeldungen/backend/.venv/bin/gunicorn --workers 3 --bind unix:/var/www/lageranmeldungen/backend/app.sock -m 007 wsgi:app
[Install]
WantedBy=multi-user.target
```
Start the service
```
sudo systemctl start lageranmeldungen-backend.service
```
Maybe this fails because of "Permission denied error" or something. You maybe need to `chown` of the socket folder

## Nginx Proxy
```
sudo nano /etc/nginx/sites-available/lageranmeldungen-backend

server {
    listen 80;
    server_name backend.zeltlager-braeunlingen.de;
location / {
        proxy_pass http://unix:/var/www/lageranmeldungen/backend/app.sock;
        include proxy_params;
        proxy_redirect off;
    }
}
```
This works for HTTP requests. To configure for HTTPS requests, some more steps need to be done:

install certbot to acquire https certificate:
```
sudo apt install certbot python3-certbot-nginx
```
Setup certbot for domain `backend.zeltlager-breaunlingen.de`:

Certbot will:
- Automatically configure SSL for you.
- Modify your Nginx config.
- Reload Nginx to apply the changes.
```
sudo certbot --nginx -d backend.zeltlager-braeunlingen.de
```

If you now check your nginx config (`/etc/nginx/sites-available/lageranmeldungen-backend`), you will notice that SSL was configured. Furthermore nginx was restarted and `/index` is reachable via HTTPS

# Useful commands
## systemctl
| Command | Description |
|---------|-------------|
| `systemctl list-units --type=service` | List services |
| `systemctl <COMMADN> <SERVICE>` | `<COMMAND>`: `start`, `stop`, `restart` a service |
| `systemctl status <SERVICE>` | Print the details about the status of a service |

## journalctl
| Command | Description |
|---------|-------------|
| `journalctl -u <SERVICE>` | Print logs of a service |

## File management
| Command | Description |
|---------|-------------|
| `ls [-l] [file]` | List files of a directory<br>- use `-l` with details/long format<br>- use `file` to get the details of a specific file |

e.g. `ls -l /var/www/lageranmeldungen/backend/app.sock` has the output:
```
srwxrwx--- 1 matze www-data 0 16. Apr 00:47 /var/www/lageranmeldungen/backend/app.sock
```
Field | Value | Meaning
------|-------|--------
`s` | `srwxrwx---` | This first letter s indicates a Unix socket file.
`rwxrwx---` |  | The permissions:<br>- rwx (owner) → matze can read/write/execute<br>- rwx (group) → www-data group can read/write/execute<br>- --- (others) → no access for anyone else
`1` |  | Hard link count (not super relevant for sockets)
`matze` |  | Owner of the file (your user)
`www-data` |  | Group associated with the file (used by Nginx)
`0` |  | Size (0 is normal for sockets)
``16. Apr 00:47`` |  | Last modification time
``/var/www/lageranmeldungen/backend/app.sock`` |  | Path to the Unix socket file
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
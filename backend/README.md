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
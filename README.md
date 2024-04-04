# Initial project setup

```
git clone https://gitlab.com/ma-hummel/lageranmeldungen.git
```

## API Specification

```
POST /registration
TODO
```

# Update Flask App on vServer
```
ssh root@backend.zeltlager-braeunlingen.de
```

## Repo updaten
```
cd /var/www/lageranmeldungen
```

## Restart Backend service
```
systemctl restart lageranmeldungen.service
```

## Check Status of Backend service
```
systemctl status lageranmeldungen.service
```
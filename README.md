### Instructions for executing the app

clone the repo

for the development environment 
supply the needed environment variables in a .env file
```
DATABASE_HOSTNAME:
DATABASE_PORT:
DATABASE_PASSWORD:
DATABASE_NAME:
DATABASE_USERNAME:
SECRET_KEY:
ALGORITHM:
ACCESS_TOKEN_EXPIRE_MINUTES:
```

then execute the following docker compose command
`docker-compose -f docker-compose-dev.yml up -d`

for the production environment 
supply the needed environment variables in production server environment as follows 
```
DATABASE_HOSTNAME:
DATABASE_PORT:
DATABASE_PASSWORD:
DATABASE_NAME:
DATABASE_USERNAME:
SECRET_KEY:
ALGORITHM:
ACCESS_TOKEN_EXPIRE_MINUTES:
```

then execute the following docker compose command
`docker-compose -f docker-compose-prod.yml up -d`

the workflow for CI/CD automation and deployment is in the `.github/workflow` directory

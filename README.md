## Setting up Rasa in Docker


1. Build Django app docker image

```
cd hr_bot
docker build -t django_app -f Dockerfile .

```

2. Build rasa-actions docker image

```
cd HRBot
docker build -t rasa-actions  -f Dockerfile .
```

3. Run docker-compose

Make sure that you have set the following env in the `.env` file in the same folder as `docker-compose.yml`

- SENDGRID_API_KEY
- RASA_SERVER


The run the following to execute all the services:

```
docker-compose up -d
```

*Note*: Please make sure that ports- 8000, 5005, 5055 are accessible.


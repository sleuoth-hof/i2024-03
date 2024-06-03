## Prerequisites

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)

## Project Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sleuoth-hof/i2024-03.git
cd i2024-03
```

### 2. Run

```bash
docker-compose up --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
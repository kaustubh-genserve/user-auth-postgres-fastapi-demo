# user-auth-postgres-fastapi-demo

Learning to implement SQLModel for PostgresSQL+FastAPI

# Create Environment & install dependancies

```
conda create -n fastapi_postgres_sqlmode python=3.12

conda activate fastapi_postgres_sqlmode

pip install -r requirements.txt
```

Create table :

```
psql -U postgres -h localhost -p 5432 -c "CREATE DATABASE testdb;"
```

# Run file

`python main.py`

# POST request for adding user

```
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 7777777777" \
  -d '{"id": 1, "name": "Alice", "email": "alice@example.com"}'
```

# Get request for fetching users

```
curl -X 'GET' \
  'http://127.0.0.1:8000/users/' \
  -H 'accept: application/json'
```

write a .env file next in needed

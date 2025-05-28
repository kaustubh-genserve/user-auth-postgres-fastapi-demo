# user-auth-postgres-fastapi-demo

Learning to implement SQLModel for PostgresSQL+FastAPI

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

```
curl -X POST "http://127.0.0.1:8000/users/" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 7777777777" \
  -d '{"id": 1, "name": "Alice", "email": "alice@example.com"}'
```

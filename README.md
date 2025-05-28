# user-auth-postgres-fastapi-demo

Learning to implement SQLModel for PostgresSQL+FastAPI

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

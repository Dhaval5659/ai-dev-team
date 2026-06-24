# FastAPI Best Practices

## Project Structure

src/
├── api/
├── services/
├── repositories/
├── models/
├── schemas/
├── core/

## Validation

* Use Pydantic models for all requests.
* Validate all user inputs.
* Return meaningful validation errors.

## Dependency Injection

* Use FastAPI Depends().
* Avoid global state.

## Database

* Use SQLAlchemy or SQLModel.
* Separate repositories from business logic.
* Use migrations.

## Security

* JWT Authentication
* Password hashing with bcrypt
* Environment variables for secrets
* Role-based authorization

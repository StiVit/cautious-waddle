# FastAPI CRUD Application

This is a FastAPI application that demonstrates basic CRUD operations with a SQLite database. The application is structured into multiple files for better organization and efficiency.

## Project Structure

CAUTIOUS-WADDLE/
├── app/
│ ├── init.py
│ ├── crud.py
│ ├── models.py
│ ├── schemas.py
│ ├── database.py
│ └── routers/
│ ├── init.py
│ └── items.py
└── main.py


## Requirements

- Python 3.8+
- FastAPI
- SQLAlchemy
- Uvicorn
- Pydantic

## Installation


- **main.py**: Main application file that initializes FastAPI and includes routers, Entry point to start the application with Uviorn.
- **app/database.py**: Database configuration and session management.
- **app/models.py**: SQLAlchemy models.
- **app/schemas.py**: Pydantic schemas for data validation.
- **app/crud.py**: CRUD operation functions.
- **app/routers/items.py**: API endpoints for items.

## Setup and Installation

### Prerequisites

- Python 3.7+
- SQLite (or another supported database)

### Installation Steps

1. **Clone the repository:**

    ```bash
    git clone https://github.com/StiVit/CAUTIOUS-WADDLE.git
    cd CAUTIOUS-WADDLE
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    python run.py
    ```

    The application will be available at `http://127.0.0.1:8000`.

## Usage

### API Endpoints

- **Create an item**

    ```http
    POST /api/items/
    ```

    Request body:

    ```json
    {
        "name": "Item name",
        "description": "Item description"
    }
    ```

- **Read an item**

    ```http
    GET /api/items/{item_id}
    ```

- **Update an item**

    ```http
    PUT /api/items/{item_id}
    ```

    Request body:

    ```json
    {
        "name": "Updated item name",
        "description": "Updated item description"
    }
    ```

- **Delete an item**

    ```http
    DELETE /api/items/{item_id}
    ```

### Swagger UI

You can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

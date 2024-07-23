# FastAPI CRUD Application

This is a FastAPI application that demonstrates basic CRUD operations with a SQLite database. The application is structured into multiple files for better organization and efficiency.

## Project Structure

CAUTIOUS-WADDLE/<br>
├── app/<br>
│ └── enumerations/ <br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── init.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── payment_method.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── product_category.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;└── region.py<br>
│ └── models/ <br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── init.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;└── models.py<br>
│ └── routers/ <br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── init.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;└── endpoints.py<br>
│ └── utils/ <br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── init.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├── config.py<br>
│ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;└── logger_config.py<br>
│ ├── init.py<br>
│ ├── crud.py<br>
│ ├── schemas.py<br>
│ └── database.py<br>
├── database/<br>
│ └── Online Sales Data.csv <br>
├── docker/<br>
│ └── docker-compose.yml <br>
├── process_csv.py <br>
├── .env.template <br>
└── main.py <br>


## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/StiVit/CAUTIOUS-WADDLE.git
    cd CAUTIOUS-WADDLE
    ```
   
2. **Run the Makefile:**

    Use the `make` command to automate the setup process.

    ```sh
    make
    ```

    This command will perform the following steps:
    - Create a virtual environment (`venv`)
    - Activate the virtual environment
    - Install the dependencies from `requirements.txt`
    - Create a `.env` file from the `.env.template`
    - Build and run the Docker containers

    **Note:** The virtual environment activation step will print a message on how to manually activate the virtual environment. Follow the instructions for your operating system:

    - On Linux and macOS:
      ```sh
      source venv/bin/activate
      ```
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```

## Manual Steps (if not using Makefile)

If you prefer to run each step manually, follow these commands:

1. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Create a `.env` file from the `.env.template`:**

    ```sh
    cp .env.template .env
    ```

4. **Build and run the Docker containers:**

    ```sh
    docker-compose up --build
    ```

Now you have your development environment set up and the application running. Enjoy coding!

### Usage

1. Launch the `main.py` file from console to transfer the data into the docker and access all the features
2. Access the application at `http://localhost:8000/docs` after starting the Docker containers.
3. Use the following endpoints to interact with the application:

    - **Create**: `POST /transactions`
    - **Create**: `POST /products`
    - **Read**: `GET /transactions/{transaction_id}`
    - **Read**: `GET /products/{product_id}`
    - **Update**: `PUT /transaction/{transaction_id}`
    - **Update**: `PUT /product/{product_id}`
    - **Delete**: `DELETE /transaction/{transaction_id}`

### Project Modules

- **app/enumerations**: Contains enumerations for various categories like payment methods, product categories, and regions.
- **app/models**: Contains the data models for the application.
- **app/routers**: Contains the API endpoints.
- **app/utils**: Contains utility functions and configurations.
- **database**: Contains the initial CSV data file.
- **docker**: Contains the Docker Compose configuration.
- **process_csv.py**: Script to process the CSV file.
- **main.py**: The main entry point of the application.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration
- References


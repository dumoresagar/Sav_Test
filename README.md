# Sav_Test


This repository contains a Django-based application designed to schedule and execute API calls at specified timestamps. It uses Celery for asynchronous task management and Redis as a message broker to handle the scheduling.

## Core Features

*   **API-driven Scheduling**: Schedule tasks by sending a POST request with timestamps to a REST endpoint.
*   **Asynchronous Execution**: Leverages Celery and Redis to run API calls in the background without blocking the main application.
*   **Task Logging**: Logs the outcome of each API call (success or failure) to a file for monitoring and debugging.
*   **Persistent Task Queue**: Scheduled tasks are stored in a database, ensuring they are not lost on application restart.
*   **Django Admin Integration**: View and manage scheduled tasks directly from the Django admin interface.

## Technology Stack

*   **Backend**: Django, Django REST Framework
*   **Task Queue**: Celery
*   **Message Broker**: Redis
*   **Database**: SQLite
*   **HTTP Requests**: `requests`

## Setup and Installation

Follow these steps to get the project running on your local machine.

### Prerequisites

*   Python 3.x
*   Redis server installed and running. By default, the application connects to `redis://localhost:6379/0`.

### Installation Steps

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/dumoresagar/Sav_Test.git
    cd Sav_Test/TIMESTAMP
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply database migrations:**
    The repository includes a pre-configured `db.sqlite3` file, but if you start from scratch, run the migrations:
    ```bash
    python manage.py migrate
    ```

### Running the Application

You need to run the Django development server and the Celery worker simultaneously. Open two separate terminal windows inside the project directory (`TIMESTAMP/`) with the virtual environment activated.

**Terminal 1: Start the Celery Worker**
```bash
celery -A Timestamps worker --loglevel=info
```

**Terminal 2: Start the Django Development Server**
```bash
python manage.py runserver
```
The application will now be running at `http://127.0.0.1:8000/`.

## Usage

### Django Admin

You can access the admin panel to view the scheduled API calls. The included database is pre-populated with an admin user.

*   **URL**: `http://127.0.0.1:8000/admin/`
*   **Username**: `admin`
*   **Password**: `admin123`

### API Endpoint

To schedule API calls, send a `POST` request to the `/api/schedule-api/` endpoint.

*   **URL**: `POST /api/schedule-api/`
*   **Description**: Schedules one or more API calls. The task will call `https://ifconfig.co`.
*   **Body**: A JSON object containing a `timestamps` key. The value should be a comma-separated string of timestamps in ISO 8601 format. Any timestamps in the past will be ignored.

#### Example `curl` Request

```bash
curl -X POST http://127.0.0.1:8000/api/schedule-api/ \
-H "Content-Type: application/json" \
-d '{"timestamps": "2025-08-01T14:30:00Z, 2025-08-01T15:00:00Z"}'
```

#### Success Response

A successful request will return a `201 CREATED` status and a JSON array of the created `ScheduledAPICall` objects.

```json
[
    {
        "id": 1,
        "timestamp": "2025-08-01T14:30:00Z",
        "status": "Pending"
    },
    {
        "id": 2,
        "timestamp": "2025-08-01T15:00:00Z",
        "status": "Pending"
    }
]
```

### Logging

The results of the API calls executed by the Celery worker are logged in the `TIMESTAMP/logs/api_calls.log` file.

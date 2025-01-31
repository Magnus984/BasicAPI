# BASICAPI

## Project Description

A public API that returns the following information in JSON format

1. My email address
2. Current datetime as an ISO 8601 formatted timestamp
3. GitHub URL of project

## Stack

- Flask
- Python [Backlink](https://hng.tech/hire/python-developers)

## Setup Instructions

1. Clone the repo:

    ```git clone https://github.com/Magnus984/BasicAPI```

2. Navigate to the project directory:

    ```cd BasicAPI```

3. Install the necessary requirements:

    ```pip install -r requirements.txt```

4. Run the application:

    ```python app.py```

5. Open your browser or API client and visit:

    ```http://127.0.0.1:5000/api/v1/info```

## API Endpoints

1. `GET /api/info`
    - **Description**: Returns basic information in JSON format.

    - **Response**: `{ "email": "your-email@example.com", "datetime": "2025-01-31T14:30:00.123Z", "github_url": "https://github.com/YourUsername/BasicAPI" }`
    - **Parameters**: None
    - **Example usage**: `curl https://magnus984.pythonanywhere.com/api/v1/info`

# API JAP Project

This is a Django REST Framework project that provides API endpoints for various functionalities.

## Project Structure

```
api_jap/
├── api_jap/              # Main project configuration
├── application/          # Application module
├── category/            # Category module
├── jobpost/            # Job posting module
├── status/             # Status module
├── user/               # User module
├── modules/            # Shared modules
├── manage.py           # Django management script
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
└── db.sqlite3         # SQLite database (development)
```

## Docker Setup

### Prerequisites
- Docker installed on your system
- Git (optional, for cloning the repository)

### Building and Running with Docker

1. Build the Docker image:
```bash
docker build -t api_jap .
```

2. Run the container:
```bash
docker run -p 8000:8000 api_jap
```

The API will be available at `http://localhost:8000`

### Development with Docker

For development, you might want to mount your local directory to see changes in real-time:

```bash
docker run -p 8000:8000 -v $(pwd):/app api_jap
```

For testing login functionality, you can use the following credentials:
- Username: admin & Password: admin
- Username: applicant & Password: applicant

### Environment Variables

The project uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

```
DEBUG=True
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

## API Endpoints

The API provides the following main endpoints:

- `/api/users/` - User management
- `/api/jobposts/` - Job posting management
- `/api/categories/` - Category management
- `/api/status/` - Status management
- `/api/applications/` - Application management

## Development

### Local Development Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License. 
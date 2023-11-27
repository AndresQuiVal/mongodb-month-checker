Certainly! Here is the README.md content in plain text:

```
# Flights Research Service

Welcome to the Flights Research Service! This application interacts with a flights API to provide information about flights and recommendations based on the most frequently visited months.

## Getting Started

These instructions will help you set up and run the Flights Research Service on your local machine.

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flights-research-service.git
   ```

2. Navigate to the project directory:

   ```bash
   cd flights-research-service
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the application by executing the `main.py` script:

```bash
python main.py [action]
```

Replace `[action]` with one of the following options:
- `list`: Retrieve a list of flights.
- `recommended`: Get recommendations based on the most frequently visited months.
- `recommended-ag`: Get recommendations using the aggregation method.

Example:

```bash
python main.py list
```

## Configuration

Make sure to set the environment variable `FLIGHTS_API_URL` to the URL of the Flights API.

```bash
export FLIGHTS_API_URL="http://localhost:8000"
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- This application was developed as part of a research project.

Feel free to customize this README.md to include additional information about your project, dependencies, or any other relevant details.
```

Copy and paste this content into your README.md file in your GitHub repository.
# DataGuard
This is a web-based tool for performing data quality checks on PostgreSQL databases. It allows users to connect to a database, select tables and columns, and run various data quality assessments.

## Features

- Connect to PostgreSQL databases
- Select tables and columns for analysis
- Perform the following data quality checks:
  - Null check
  - Numeric distribution analysis
  - Inaccurate data detection (improper characters)
  - Data variety assessment
- Web-based interface using Bootstrap for responsive design

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- pip (Python package manager)
- PostgreSQL database for testing

## Installation

1. Clone this repository:
git [https://github.com/Steven-Nanga/DataGuard/tree/master]
cd DataGuard
Copy
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install the required packages:
pip install -r requirements.txt

## Usage

1. Start the Flask application:
python app.py
Copy
2. Open a web browser and navigate to `http://localhost:5000`

3. Enter your PostgreSQL database credentials and connect

4. Select a table and columns to analyze

5. Choose the data quality checks you want to perform

6. Click "Run Checks" to see the results

## Project Structure

- `app.py`: The main Flask application
- `templates/index.html`: The HTML template for the web interface
- `requirements.txt`: List of Python dependencies

## Contributing

Contributions to the Data Quality Check Tool are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature-name`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature-name`)
6. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please open an issue on GitHub.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [Bootstrap](https://getbootstrap.com/)
- [psycopg2](https://www.psycopg.org/)
- [pandas](https://pandas.pydata.org/)

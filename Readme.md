
# Django CSV File Upload and Display

This Django project allows users to upload a CSV file, and it displays the content of the uploaded CSV in an HTML table.

## Features

- CSV file upload functionality using Django forms.
- Display uploaded CSV content in a formatted HTML table.

## Prerequisites

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aniketArun/Python-Mini-Projects.git
   cd csvdisp
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Run the development server:

   ```bash
   python manage.py runserver
   ```

## Usage

1. Navigate to the file upload page by visiting:

   ```
   http://localhost:8000/
   ```

2. Upload a CSV file from your local system.

3. After uploading, the contents of the CSV file will be displayed in an HTML table.

## File Structure

- `forms.py`: Contains the form for handling file uploads.
- `views.py`: Defines the view to handle CSV file upload and data processing.
- `templates/`: Contains the HTML templates for uploading the file and displaying the data.
  - `base.html`: Form for uploading the CSV file.
  - `index.html`: Displays the CSV file content in a table format.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for suggestions and improvements.

## Contact
    aniketpen8478@gmail.com

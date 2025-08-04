# SenseHat Web Server

This project sets up a simple web server on a Raspberry Pi 3 using Flask and the SenseHat library to read and display temperature and humidity data.

## Project Structure

```
sensehat-webserver
├── src
│   ├── app.py            # Main entry point of the web server
│   ├── sense_reader.py    # Functions to read data from SenseHat
│   ├── static
│   │   └── main.js       # JavaScript for updating the webpage
│   └── templates
│       └── index.html    # HTML template for the web page
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to have the following installed:

- Python 3
- pip

## Setup Instructions

1. Clone the repository or download the project files to your Raspberry Pi.

2. Navigate to the project directory:

   ```bash
   cd sensehatpage
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Running the Server

To start the web server, run the following command:

```bash
python src/app.py
```

The server will start and listen on `http://localhost:5000`.

## Accessing the Web Page

Open a web browser and navigate to `http://<your-raspberry-pi-ip>:5000` to view the temperature and humidity data. The page will automatically update with new values every few seconds.

## License

This project is licensed under the MIT License.
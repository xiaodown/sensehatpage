# SenseHat Web Server

This project sets up a simple, attractive web server on a Raspberry Pi 3 using Flask and the Sense HAT library. It reads temperature (with CPU heat compensation) and humidity, and displays them in real time on a modern, auto-updating web page.

---

## Features

- **Live Temperature & Humidity:** Readings from the Sense HAT, with temperature corrected for CPU heat.
- **Modern Web UI:** Large, color-coded, easy-to-read display, auto-refreshing every 5 seconds.
- **Responsive Design:** Looks great on desktop, tablet, or phone.
- **No Scrollbars:** Clean, centered layout.
- **Simple Setup:** Only major, Pi-compatible libraries required.

---

## Project Structure

```
sensehatpage/
├── src/
│   ├── app.py             # Flask web server
│   ├── sense_reader.py    # Sensor reading and compensation logic
│   ├── static/
│   │   └── main.js        # JavaScript for live updates
│   └── templates/
│       └── index.html     # Responsive, styled web page
├── requirements.txt       # Python dependencies
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## Requirements

- Raspberry Pi 3 (or compatible) with Sense HAT
- Python 3
- [uv](https://github.com/astral-sh/uv) (for fast virtualenv and dependency management)

---

## Setup Instructions

1. **Clone or copy this repository to your Raspberry Pi.**

2. **Navigate to the project directory:**
   ```bash
   cd sensehatpage
   ```

3. **Create and activate a virtual environment using uv:**
   ```bash
   uv venv
   source .venv/bin/activate
   ```

4. **Install dependencies with uv:**
   ```bash
   uv pip install -r requirements.txt
   ```

   This will install Flask, sense-hat, and RTIMULib (for Sense HAT support).

---

## Running the Server

Start the web server with:
```bash
python src/app.py
```
The server will listen on `http://0.0.0.0:5000` (all network interfaces).

---

## Viewing the Web Page

Open a browser on any device on your network and go to:
```
http://<your-raspberry-pi-ip>:5000
```
You’ll see a live, auto-updating display of temperature (in °F) and humidity (%), each in a large, color-coded box.

---

## How Temperature Correction Works

The Sense HAT’s temperature sensor can be affected by CPU heat. This project compensates by reading the CPU temperature and applying a correction formula:

```
corrected_temp = raw_temp - ((cpu_temp - raw_temp) / 1.5)
```
You can tune the divisor (`1.5`) in `sense_reader.py` for your setup.

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [Sense HAT Python](https://pythonhosted.org/sense-hat/)
- [RTIMULib](https://github.com/RPi-Distro/RTIMULib)
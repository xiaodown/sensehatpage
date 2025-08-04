const updateSensorData = async () => {
    try {
        const response = await fetch('/sensor-data');
        const data = await response.json();
        
        document.getElementById('temperature').innerText = `Temperature: ${data.temperature} °C`;
        document.getElementById('humidity').innerText = `Humidity: ${data.humidity} %`;
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
};

setInterval(updateSensorData, 5000); // Update every 5 seconds

document.addEventListener('DOMContentLoaded', updateSensorData); // Initial fetch on page load
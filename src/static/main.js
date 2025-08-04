const updateSensorData = async () => {
    try {
        const response = await fetch('/data'); 
        const data = await response.json();
        
        document.getElementById('temperature').innerText = data.temperature;
        document.getElementById('humidity').innerText = data.humidity;
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
};

setInterval(updateSensorData, 5000); // Update every 5 seconds

document.addEventListener('DOMContentLoaded', updateSensorData); // Initial fetch on page load
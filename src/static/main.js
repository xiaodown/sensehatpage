const updateSensorData = async () => {
    try {
        const response = await fetch('/data'); 
        const data = await response.json();
        
        document.getElementById('temperature').innerText = Number(data.temperature).toFixed(1);
        document.getElementById('humidity').innerText = Number(data.humidity).toFixed(1);
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
};

setInterval(updateSensorData, 5000); // Update every 5 seconds

document.addEventListener('DOMContentLoaded', updateSensorData); // Initial fetch on page load

document.addEventListener('DOMContentLoaded', function () {
    fetch('http://127.0.0.1:8000/tradeprice/')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            console.log('Received data:', data);
    
            const labels = data.map(entry => entry.timestamp);

            const currentPrices = data.map(entry => parseFloat(entry.currentPrice));

            const entryPrices = data.map(entry => parseFloat(entry.entryPrice));

            
            const ctx = document.getElementById('myChart').getContext('2d');
            
            const myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Current Price',
                            data: currentPrices,
                            borderColor: 'blue',
                            backgroundColor: 'rgba(0, 0, 255, 0.1)',
                            borderWidth: 2,
                            pointRadius: 3,
                            fill: false
                        },
                        {
                            label: 'Entry Price',
                            data: entryPrices,
                            borderColor: 'green',
                            backgroundColor: 'rgba(0, 255, 0, 0.1)',
                            borderWidth: 2,
                            pointRadius: 3,
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    plugins: {
                        tooltip: {
                            mode: 'index',
                            intersect: false
                        }
                    },
                    scales: {
                        x: {
                            display: true,
                            title: {
                                display: true,
                                text: 'Timestamp'
                            }
                        },
                        y: {
                            display: true,
                            title: {
                                display: true,
                                text: 'Price'
                            }
                        }
                    }
                }
            });
        })
        .catch(error => console.error('Error fetching data:', error));
});

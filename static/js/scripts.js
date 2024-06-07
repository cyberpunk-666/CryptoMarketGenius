document.addEventListener('DOMContentLoaded', function () {
    // Fetch data from Flask server (which in turn fetches from Kraken API)
    fetch('/kraken/balance')
        .then(response => response.json())
        .then(data => {
            // Process data here
            console.log(data); // Example to show the balance data in the console

            // Example: Create a chart with dummy data
            var ctx = document.getElementById('myChart').getContext('2d');
            var myChart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
                    datasets: [{
                        label: 'Prix Bitcoin',
                        data: [30000, 32000, 31000, 35000, 37000, 39000, 41000],
                        backgroundColor: 'rgba(0, 255, 204, 0.2)',
                        borderColor: 'rgba(0, 255, 204, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    scales: {
                        y: {
                            beginAtZero: false
                        }
                    }
                }
            });

            // Portfolio Chart
            if (document.getElementById('portfolioChart')) {
                var portfolioCtx = document.getElementById('portfolioChart').getContext('2d');
                var portfolioChart = new Chart(portfolioCtx, {
                    type: 'bar',
                    data: {
                        labels: ['Stock A', 'Stock B', 'Stock C', 'Crypto A', 'Crypto B'],
                        datasets: [{
                            label: 'Performance',
                            data: [12, 19, 3, 5, 2],
                            backgroundColor: 'rgba(75, 192, 192, 0.2)',
                            borderColor: 'rgba(75, 192, 192, 1)',
                            borderWidth: 1
                        }]
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });
            }
        })
        .catch(error => console.error('Error fetching data:', error));
});
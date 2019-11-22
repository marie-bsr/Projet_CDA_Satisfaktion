
// Global parameters:
// do not resize the chart canvas when its container does (keep at 600x400px)
Chart.defaults.global.responsive = false;


function affichePie(results, element) {
    var ctx = element;
    var myChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['Très insuffisant', 'Insuffisant', 'Acceptable', 'Satisfaisant', 'Excellent'],
            datasets: [{
                label: '# of Votes',
                data: results,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(235, 127, 54, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'

                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(235, 127, 54, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'

                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

//fonction graphique en bar
function graphBar(results, element) {

    var ctx = element;
    var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Très insuffisant', 'Insatisfaisant', 'Acceptable', 'Satisfaisant', 'Excellent'],
            datasets: [{
                label: 'SATISFAKTION sur la progression',
                data: results,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}

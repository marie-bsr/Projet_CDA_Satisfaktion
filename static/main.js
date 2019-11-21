

//Fonction pour créer des messages de confirmation à l'utilisateur
function envoiConfirmation(message){
    if(confirm(message)){
        alert("Envoi confirmé !")
// Renvoyer a la page precedente
    }else{
//Renvoyer a la page precedente / cacher l'alert
    }
}


//Fonction pour créer des alertes utilisateur
function envoiMessage(message){
    alert(message)
}

//fonction graphique en bar
function graphBar (results){
                
                var ctx = document.getElementById('myChart');
                var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [ 'Très insuffisant', 'Insatisfaisant', 'Acceptable', 'Satisfaisant', 'Excellent'],
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
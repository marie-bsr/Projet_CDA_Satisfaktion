

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
document.querySelector('button').onclick = function() {
    console.log("Fetching to API...");

    const question = document.getElementById('poll-question').value
    const userId = document.getElementById('user-id').value
    const choices = Array.from(document.querySelectorAll('.poll-choice'))
    .map(function(choice){
        return choice.value
    })
    .filter(function(choice){
        return choice
    }) 


if (!question || choices.length <2) {
    alert('Enter poll question and atleast two choices')
    return
}
console.log("Sending this data:", {
  question,
  choices,
  user_id: userId
});


fetch('http://127.0.0.1:8002/polls/api/create-poll/', {
    method : 'POST',
    headers : {
        'Content-Type' : 'application/json',
    },
    body: JSON.stringify({
        question , choices , user_id : userId
    })
}
)


.then(res => res.json())
.then(function(data){
    if (data.message){
        alert(data.message)
    }
    else {
        alert('Pole created') 
    }
})}
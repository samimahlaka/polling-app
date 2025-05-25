const BASE_URL = "https://polling-app-batu.onrender.com";


document.getElementById('result-btn').addEventListener('click', function(){
    const pollId = document.getElementById('poll-id').value

    if (!pollId){
    alert('No such poll id exist')
    return
    }   

    fetch(`${BASE_URL}/polls/api/result/${pollId}/`,
        {
            method : 'GET' ,
            headers : {
                'Content-Type' : 'application/json',
            },
        }
    )

    .then(function(response){
        if (!response.ok) {
            throw new Error('Poll not found');  
        }
        return response.json()
    })

    .then(function(poll){
        let resultContainer = document.getElementById('result-container')
        resultContainer.innerHTML += `POLL: ${poll.question}`

        poll.choices.forEach(function(choice){
            resultContainer.innerHTML += `<li> ${choice.text} : ${choice.vote} votes </li>`
        })
    })
})
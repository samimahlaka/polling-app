

fetch('http://127.0.0.1:8003/polls/api/poll_list/')


.then(function(response){
    console.log(response)
    return response.json()
})


.then(function(data){
    const container = document.getElementById('poll-container')
    data.forEach(function(poll){
        let pollhtml = '<div>'
        pollhtml += '<h3>' + poll.question + '</h3>'

        let choicehtml = ''

        poll.choices.forEach(function(choice){
            choicehtml += '<label>'
            choicehtml += '<input type = "radio" value = "' + choice.id + '"  name = "' + poll.id + '" >'
            choicehtml += choice.text
            choicehtml += '</label>' + '<br>' 
        })
        pollhtml += choicehtml;
        pollhtml += '</div>'
        container.innerHTML += pollhtml

    })
})


document.querySelector('button').addEventListener('click', function(){
    const selected = document.querySelectorAll("input[type = 'radio']:checked")

    if (selected.length == 0) {
        alert('Please select one option per poll')
        return
    }
    const votes = Array.from(selected).map(function(input){
        return {choice_id : input.value}
    })

    Promise.all(
        votes.map(function(vote){
                return fetch (`http://127.0.0.1:8003/polls/api/vote/${vote.choice_id}/`, 
                {
                    method : 'POST',
                    headers : {
                        'Content-Type' : 'application/json',
                        'X-CSRFToken' : getCSRFToken(),
                    },
                    body : JSON.stringify({})
                })

        })
    )
    .then(function(){
        window.location.href = 'thankyou.html' 
    })
})

function getCSRFToken() {
  const name = 'csrftoken';
  const cookie = document.cookie
    .split('; ')
    .find(row => row.startsWith(name + '='));
  return cookie ? cookie.split('=')[1] : '';
}

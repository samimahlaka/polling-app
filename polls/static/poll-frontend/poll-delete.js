document.getElementById('del-btn').addEventListener('click', function(){
    const pollId = document.getElementById('poll_id').value

    if (!pollId) {
        alert('Please enter valid poll id')
        return
    }

    fetch(`http://127.0.0.1:8004/polls/api/poll_delete/${pollId}/`,
        {
            method : 'DELETE',
            headers : {
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify({})
        })

        .then(function(response){
            if(response.ok) {
                document.getElementById('result').innerText = `Poll id : ${pollId} deleted successfully`
            } 
            else {
                document.getElementById('result').innerText = `Failed to delete poll ${pollId} `
            } 

        })  



    
})
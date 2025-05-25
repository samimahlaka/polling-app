const BASE_URL = "https://polling-app-batu.onrender.com";


document.getElementById('update-btn').addEventListener('click', function () {
    const pollId = document.getElementById('poll-id').value;

    if (!pollId) {
        return console.error('PLEASE ENTER VALID POLL ID');
    }

    fetch(`${BASE_URL}/polls/api/poll_detail/${pollId}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(function (response) {
        if (!response.ok) {
            throw new Error('Poll not found');
        }
        return response.json();
    })
    .then(function (poll) {
        const container = document.getElementById('update-container');
        container.innerHTML = '';

        container.innerHTML += `
            <label>Question:</label>
            <input type="text" id="poll_question" value="${poll.question}" /><br><br>
        `;

        poll.choices.forEach(function (choice, index) {
            container.innerHTML += `
                <label>Choice ${index + 1}:</label><br>
                <input 
                    type="text" 
                    class="choice-input" 
                    value="${choice.text}" 
                    data-id="${choice.id}"
                /><br><br>
            `;
        });

        container.innerHTML += `<button id="submit-btn">Submit Update</button>`;

        // ✅ attach event listener after button is created
        document.getElementById('submit-btn').addEventListener('click', function () {
            const updatedQuestion = document.getElementById('poll_question').value;

            const updatedChoices = Array.from(document.getElementsByClassName('choice-input')).map(function (choice) {
                return {
                    id: choice.dataset.id,
                    text: choice.value
                };
            });

            fetch(`${BASE_URL}/polls/api/poll_update/${pollId}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCSRFToken(),
                },
                body: JSON.stringify({
                    question: updatedQuestion,
                    choices: updatedChoices
                })
            })
            .then(function (response) {
                return response.json().then(function (data) {
                    if (response.ok) {
                        alert(data.message);
                    } else {
                        alert("Update failed: " + data.message);
                    }
                });
            })
            .catch(function (error) {
                alert("Something went wrong: " + error.message);
            });
        });
    })
    .catch(function (error) {
        alert(error.message);
    });
});

function getCSRFToken() {
    const name = 'csrftoken';
    const cookie = document.cookie
        .split('; ')
        .find(row => row.startsWith(name + '='));
    return cookie ? cookie.split('=')[1] : '';
}

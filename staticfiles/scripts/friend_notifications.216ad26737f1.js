$(document).ready(function () {
    function sendFriendRequest(userId) {
        fetch(`/friends/send/${userId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'sent') {
                alert('Friend request sent!');
            } else if (data.status === 'already_sent') {
                alert('Friend request already sent.');
            }
        })
        .catch(error => console.error('Error:', error));
    }
    
    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function checkFriendRequests() {
        fetch('/friends/get/')
        .then(response => response.json())
        .then(data => {
            // Update your notification display here
            console.log(data);  // For now, just log the data
        });
    }
    
    // Check for new friend requests every 30 seconds
    setInterval(checkFriendRequests, 30000);
});

$(document).ready(function(){
    let sidebar = $(".sidebar");
    let sidebar_close = $(".sidebar_close");
    let sidebar_container = $(".sidebar_container");
    let add_friend= $("#add_friend")
    let isFriend = false;
    sidebar.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "block");
        sidebar.css("display", "none");
        sidebar_container.css("display","flex");
        sidebar_close.css("display", "block");
    });

    sidebar_close.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "none");
        sidebar_close.css("display", "none");
        sidebar_container.css("display","none");
        sidebar.css("display", "block");
    });

    add_friend.on("click", function(e){
        e.preventDefault();
        if (isFriend) {
            // If already a friend, change to add friend icon
            add_friend.html('<i class="bi bi-person-add"></i>');
            isFriend = false;
        } else {
            // If not a friend, change to remove friend icon
            add_friend.html('<i class="bi bi-person-fill-x"></i>');
            isFriend = true;
        }
    });
    document.addEventListener('DOMContentLoaded', function() {
        const addFriendButton = document.getElementById('add_friend');
        const friendStatus = document.getElementById('friend_status');
        let isFriendRequested = false;
    
        addFriendButton.addEventListener('click', function() {
            const userId = this.getAttribute('data-user-id');
            const url = isFriendRequested ? `/friend_requests/cancel/${userId}/` : `/friend_requests/send/${userId}/`;
    
            fetch(url, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json'
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'sent' || data.status === 'cancelled') {
                    isFriendRequested = !isFriendRequested;
                    updateButtonState();
                }
            })
            .catch(error => console.error('Error:', error));
        });
    
        function updateButtonState() {
            if (isFriendRequested) {
                friendStatus.textContent = 'Cancel Request';
                addFriendButton.classList.add('requested');
            } else {
                friendStatus.textContent = 'Add Friend';
                addFriendButton.classList.remove('requested');
            }
        }
    
        // Function to get CSRF token from cookies
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
    });
});

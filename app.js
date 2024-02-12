document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch and display wallet balance
    function fetchBalance() {
        fetch('getBalance.php')
            .then(response => response.json())
            .then(data => {
                document.getElementById('balance').textContent = `Balance: $${data.balance.toFixed(2)}`;
            })
            .catch(error => console.error('Error fetching wallet balance:', error));
    }

    // Function to update notification preference
    function updateNotificationPreference() {
        const notificationEnabled = document.getElementById('notification-checkbox').checked;
        fetch('updateNotificationPreference.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ notificationEnabled }),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Notification preference updated:', data);
        })
        .catch(error => console.error('Error updating notification preference:', error));
    }

    // Fetch initial balance when the page loads
    fetchBalance();

    // Attach event listener to the notification checkbox
    document.getElementById('notification-checkbox').addEventListener('change', updateNotificationPreference);
});

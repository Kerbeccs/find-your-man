function saveChanges() {
    console.log('Save button clicked');
}

$(document).ready(function() {
    $('#profileForm').submit(function(event) {
        event.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            url: '/student/profile/',
            type: 'POST',
            data: formData,
            success: function(response) {
                console.log('Profile data submitted successfully!');
                alert('Profile data submitted successfully!');
            },
            error: function(error) {
                console.error('Failed to submit profile data:', error);
                alert('Failed to submit profile data. Please try again.');
            }
        });
    });
});

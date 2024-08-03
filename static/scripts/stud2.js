$(document).ready(function() {
    $('#achievementForm').submit(function(event) {
        event.preventDefault();

        const formData = $(this).serialize();

        $.ajax({
            url: '/academicinfo/',
            type: 'POST',
            data: formData,
            success: function(response) {
                console.log('Achievement data submitted successfully!');
                alert('Achievement data submitted successfully!');
            },
            error: function(xhr, status, error) {
                console.error('Failed to submit achievement data:', error);
                alert('Failed to submit achievement data. Please try again.');
            }
        });
    });
});

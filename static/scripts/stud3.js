function loadContent(url, title) {
    $.get(url, function(data) {
        $('#content').html(data);
        document.title = title;
        history.pushState({ url: url, title: title }, title, url);
    });
}

$(window).on('popstate', function(event) {
    if (event.originalEvent.state) {
        const { url, title } = event.originalEvent.state;
        loadContent(url, title);
    }
});

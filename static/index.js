document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("login").addEventListener("submit", logon);
    document.getElementById("btn_get").addEventListener("click", httpFetch);
    document.getElementById("btn_post").addEventListener("click", httpFetch);
    document.getElementById("btn_delete").addEventListener("click", httpFetch);
});

function logon(event) {
    event.preventDefault();
    const loginForm = document.getElementById(this.id);
    const formData = new FormData(loginForm);
    const data = new URLSearchParams(formData);
    let output = '';
    fetch("./login",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: data
        })
        .then(function (response) {
            output += "HTTP-Statuscode: " + response.status;
            if (response.ok) {
                return response.text();
            }

        })
        .then(function (data) {
            output += "<br/>" + "Token: " + data;
            sessionStorage.setItem("token", data);
        })
        .catch(function (error) {
            console.log(error);
        })
        .finally(() => {
            document.getElementById("response").innerHTML = output;
        });

}

function httpFetch(event) {
    const buttonId = this.id;
    let httpMethod = "";
    if (buttonId == "btn_get") {
        httpMethod = "GET";
    } else if (buttonId == "btn_post") {
         httpMethod = "POST";
    } else {
         httpMethod = "DELETE";
    }
    let output = '';
    fetch("http://127.0.0.1:5001",
        {
            method: httpMethod,
            headers: {
                "Authorization": "Bearer " + sessionStorage.getItem("token")
            }
        })
        .then(function (response) {
            output += "HTTP-Statuscode: " + response.status;
            if (response.ok) {
                return response.text();
            }

        })
        .then(function (data) {
            output += "<br/>" + "Message: " + data;
        })
        .catch(function (error) {
            console.log(error);
        })
        .finally(() => {
            document.getElementById("response2").innerHTML = output;
        });
}
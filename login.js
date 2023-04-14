window.onload = function() {
    server_name = "http://us.hio01.botshard.com:10004";
    // make server_name global
    window.server_name = server_name;
}

function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    $.ajax({
        url: server_name + '/login?username=' + username + '&password=' + password,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
            // make username global
            window.username = username;
        }
    });
}

function validateRegister() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const password2 = document.getElementById("password2").value;

    if (password === password2 && username !== "" && password !== "") {
        fetch(server_name + '/register?username=' + username + '&password=' + password)
            .then(response => response.json())
            .then(data => {
                // check if data is "code": 1
                if (data.code === 1) {
                    // clear the fields
                    document.getElementById("username").value = "";
                    document.getElementById("password").value = "";
                    document.getElementById("password2").value = "";
                    alert("Username already exists!");
                } else {
                    // alert account created
                    alert("Account created!");
                    // load login page
                    load_login();
                }
            });
    } else {
        alert("Passwords do not match!");
    }
}

function load_login() {
    // open login.html
    window.location.href = "login.html";
}

function viewRecipes() {
    $.ajax({
        url: server_name + '/view_recipes?username=' + username,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function back() {
    $.ajax({
        url: server_name + '/back?username=' + username,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function addRecipe() {
    $.ajax({
        url: server_name + '/addRecipe?username=' + username,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function add_recipe() {
    recipe = document.getElementById("recipe").value;
    $.ajax({
        url: server_name + '/add_recipe?username=' + username + '&recipe=' + recipe,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function deleteRecipe(recipe) {
    $.ajax({
        url: server_name + '/deleteRecipe?username=' + username + '&recipe=' + recipe,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function changeRecipe(recipe) {
    // make recipe global and call it 'old_recipe'
    window.old_recipe = recipe;
    $.ajax({
        url: server_name + '/changeRecipe?username=' + username + '&recipe=' + recipe,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}

function change_recipe(recipe) {
    $.ajax({
        url: server_name + '/change_recipe?username=' + username + '&recipe=' + recipe + '&old_recipe=' + old_recipe,
        type: 'GET',
        success: function(response) {
            $('.week').html(response);
        }
    });
}
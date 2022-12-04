s = 0;
m = 0;
h = 0;

function changeImg() {
    if (document.getElementById("btn").value == "Start"){
        document.getElementById("btn").value = "Stop"
        document.getElementById("btn").style.backgroundColor = "#FF0000";
        document.getElementById("btn").style.borderColor = "#FF0000";
        s, m, h = setTimeout(contTimer, 1000, s, m, h);
    }
    else if (document.getElementById("btn").value == "Stop"){
        document.getElementById("btn").value = "Start"
        document.getElementById("btn").style.backgroundColor = "#00FF00";
        document.getElementById("btn").style.borderColor = "#00FF00";
    };
};

function contTimer(s, m, h) {

    if (s < 60) {
        s += 1;
    }
    else if (s >= 59 && m < 60) {
        s = 0;
        m += 1;
    }
    else {
        s = 0;
        m = 0;
        h += 1;
    };

    time = h?.toString() + " : " + m?.toString() + " : " + s?.toString();
    document.getElementById("time").textContent = time;

    if (document.getElementById("btn").value == "Stop") {
        s, m, h = setTimeout(contTimer, 1000, s, m, h);
    }
    else {
        return s, m, h;
    };
};
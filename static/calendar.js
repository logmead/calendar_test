function changeVisibility(element) {

    if (typeof element === "string") {

            element = document.getElementById(element);
    }
    if (element) {
            element.hidden = !(element.hidden);
    } else {
            console.log("In changeVisibility: element not found");
    }
}


function pairVisibility(element) {

    let first = element.dataset.first;
    let second = element.dataset.second;
    let third = document.getElementById(element.dataset.third);

    console.log(third);

    if (third.hidden) {
        changeVisibility(first);
        changeVisibility(second);
    } else {
        changeVisibility(third);
        changeVisibility(first);
    }
}


function initialCalendar() {

	

	console.log("got to the initial calendar");
    let targetEl = document.getElementById("cal-placeholder");

    let prom = htmx.ajax('GET', targetEl.dataset.url, {target: targetEl, swap : 'outerHTML'});


}

function sendForm(caller) {
	
    let targetEl = document.getElementById("calendar-object");
    



    console.log("reached sendForm");
    
    let dat_str = caller.dataset.sub;
    
    console.log(dat_str);

    let el = document.getElementById('id_date_field');
    el.value = dat_str;

    let formEl = document.getElementById("calendar-form");
    let val = htmx.values(formEl);
    let url = formEl.dataset.url;

    let prom = htmx.ajax('POST', url, {target : targetEl, source : formEl, values : val, swap: 'outerHTML'});
	

}

function showOneTable(caller) {
	let id = caller.dataset.id;
	let tables = document.getElementsByClassName("alert-dropdown");

	for (let i = 0; i < tables.length; i++) {
		if (tables[i].id != id && !tables[i].hidden) { changeVisibility(tables[i]); }
		if (tables[i].id === id && tables[i].hidden) { changeVisibility(tables[i]); }
	}

}



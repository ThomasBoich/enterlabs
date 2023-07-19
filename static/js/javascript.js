const dropDown = document.getElementById('dropdown');

dropDown.addEventListener('click', function () {
    document.getElementById('drop-down').classList.toggle("active");
});

const newElem = document.getElementById('newEL');
newElem.addEventListener("click", addEl);

function addEl() {

    let elem = document.createElement("div");
    elem.classList.toggle('el1');
    elem.innerHTML = `
    <div class="order" id="order">
        <select name="" class="custom-select" id="custom-select">
            <option selected disabled>Тип анализа</option>
            <option value="1">Какой-то текст</option>
            <option value="2">Что-то ещё</option>
        </select>
        <input type="file" id="" name="" />
    </div>`;

    let parentGuest = document.getElementById("el1");
    parentGuest.parentNode.insertBefore(elem, parentGuest.nextSibling);

};

const newElPlus = document.getElementById('newElPlus');
newElPlus.addEventListener("click", addElPlus);

function addElPlus() {
    let elem = document.createElement("div");
    elem.classList.toggle('el1');
    elem.innerHTML = `
    <div class="order" id="order">
        <select name="" class="custom-select" id="custom-select">
            <option selected disabled>Тип анализа</option>
            <option value="1">Какой-то текст</option>
            <option value="2">Что-то ещё</option>
        </select>
        <input type="text" id="" name="" />
    </div>`;

    let parentGuest = document.getElementById("el1");
    parentGuest.parentNode.insertBefore(elem, parentGuest.nextSibling);
};

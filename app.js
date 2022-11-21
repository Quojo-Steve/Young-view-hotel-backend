const del = document.querySelectorAll('.delete');
const act = document.querySelectorAll('.activate');
const display = document.querySelector('.form');
const display1 = document.querySelector('.form1');
const remove = document.querySelector('.no');
const remove1 = document.querySelector('.no1');

act.forEach((btn) => {
    btn.addEventListener('click', () => {
        display1.classList.remove('remove')
    })
});
del.forEach((btn) => {
    btn.addEventListener('click', () => {
        display.classList.remove('remove')
    })
});
remove.addEventListener('click', () => {
    display.classList.add('remove')
})
remove1.addEventListener('click', () => {
    display1.classList.add('remove')
})

window.addEventListener("resize", function(){
    alert("This page isnt responsive")
  });
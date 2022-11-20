const del = document.querySelectorAll('.delete');
const display = document.querySelector('.form');
const remove = document.querySelector('.no');

del.forEach((btn)=>{
    btn.addEventListener('click', () => {
        display.classList.remove('remove')
    })
})
remove.addEventListener('click', () => {
    display.classList.add('remove')
})

window.addEventListener("resize", function(){
    alert("This page isnt responsive")
  });
const panels = document.querySelectorAll('.panel')  //定義物件

panels.forEach((panel)=> {
    
    panel.addEventListener('click',()=>{
        removeActiveClass()  //先將所有的移除 
        panel.classList.add('active')  //再加上class 
    })
})

function removeActiveClass(){
    panels.forEach(panel=>{
        panel.classList.remove('active')
    })
}
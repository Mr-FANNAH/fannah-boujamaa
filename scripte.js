


let section = document.querySelectorAll('section');
let navlinks = document.querySelectorAll('header nav a');
window.onscroll = () =>{
    section.forEach(sec =>{
        let top = window.scrollY;
        let offst = sec.offsetTop-150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(to >= offst && top <offset +height){
            navlinks.forEach(links=>{
                links.classList.remove('active');
                document.querySelector(Header nav a[href*=' + id +']).classList.add('active');

            });
        };
    });
};
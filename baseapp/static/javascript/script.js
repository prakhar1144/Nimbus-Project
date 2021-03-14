//var i = 0;
//var txt = "ELECTRICITY BOARD"
//var speed = 100;

//function typeWriter() {
  //  if(i < txt.length)
    //{
      //  document.getElementById("animate").innerHTML += txt.charAt(i);
        //i++;
        //setTimeout(typeWriter, speed);
    //}
//}

//typeWriter();

const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  var e = document.querySelector(".content");
  if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';

  
});
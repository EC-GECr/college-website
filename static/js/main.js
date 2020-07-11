
// Navigation Menu
const menuBtn = document.querySelector(".menu-btn");
const closeBtn = document.querySelector(".close-btn");
const menu = document.querySelector(".menu");
const navItems = document.querySelectorAll(".nav-item0");


menuBtn.addEventListener('click', openMenu);
closeBtn.addEventListener('click', closeMenu);

function openMenu(){ 
  menu.classList.add("show");
  navItems.forEach(item => item.classList.add('show'));

  menuBtn.classList.add("close");
}

function closeMenu(){ 
  menu.classList.remove("show");
  navItems.forEach(item => item.classList.remove('show'));
  
  menuBtn.classList.remove("close");
}


// Register Form
let j = 0;

$(".clicker").click(function () {

  let $btn = $(this),
    $step = $btn.parents(".card-body"),
    stepIndex = $step.index(),
    $pag = $(".card-header span").eq(stepIndex);

  let form_box;
  let alert_box;

  console.log(j);
  if(j === 0) {
    form_box = document.querySelector('#form-1');
    alert_box = document.querySelector('.msg-box-1');
  }
  if(j === 1) {
    form_box = document.querySelector('#form-2');
    alert_box = document.querySelector('.msg-box-2');
  }
  if(j === 2) {
    form_box = document.querySelector('#form-3');
    alert_box = document.querySelector('.msg-box-3');
  }

  let allAreFilled = true;

  form_box.querySelectorAll("[required]").forEach(function (i) {
    if(!allAreFilled) return;
    if(!i.value) allAreFilled = false;
  });

  if(!allAreFilled){
    alert_box.classList.add('show-alert');
  }

  else{
    if (
        stepIndex === 0 ||
        stepIndex === 1 ||
        stepIndex === 2 ||
        stepIndex === 3
    ) {
      step1($step, $pag, stepIndex);
    }
    alert_box.classList.remove('show-alert');
    j++;
  }
});

function step1($step, $pag, stepIndex) {

  // animate the step out
  $step.addClass("animate-out");

  // animate the step in
  setTimeout(function () {
    $step.removeClass("animate-out is-showing").next().addClass("animate-in");

    $pag.removeClass("is-active").next().addClass("is-active");

    if (stepIndex === 3) {
      $(".card-header span").addClass("is-active");
    }
  }, 600);

  // after the animation, adjust the classes
  setTimeout(function () {
    $step.next().removeClass("animate-in").addClass("is-showing");
  }, 1200);
}

function step3($step, $pag) {
  // animate the step out
  $step.parents(".card").addClass("animate-up");
}


// Back-to-top Button
const btn = $("#back-to-top");

$(window).scroll(function () {
  if ($(window).scrollTop() > 200) {
    btn.addClass("show");
  } else {
    btn.removeClass("show");
  }
});

btn.on("click", function (e) {
  e.preventDefault();

  $("html, body").animate({ scrollTop: 0 }, "300");
});

// To Career Map Scroll
const mapBtn = $('#careerMap');
const homeContainer = $('.home-body-container');

$('.scrollTo').click(function(){
  mapBtn.addClass("show");
  homeContainer.addClass("rm-mb");

  $('html, body').animate({
      scrollTop: $( $(this).attr('href') ).offset().top
  }, 500);
  return false;
});

// // To animate the header on scroll

// // Setup a timer
// var timeout;

// // Listen for resize events
// window.addEventListener('scroll', function ( event ) {

// 	// If there's a timer, cancel it
// 	if (timeout) {
// 		window.cancelAnimationFrame(timeout);
// 	}

//     // Setup the new requestAnimationFrame()
// 	timeout = window.requestAnimationFrame(function () {

//         // Run our scroll functions

//     let scrollPosition = Math.round(window.scrollY);
    
//     console.log(scrollPosition);
//     if (scrollPosition > 175){
//       $(".header-big").addClass('close');
//     }
//     else {
//       $(".header-big").removeClass('close');
// }

//     if (scrollPosition > 280){
//       $(".header-sm").addClass('show');
//     }
//     else {
//       $(".header-sm").removeClass('show');
//     }

// });

// }, false);
// window.addEventListener('resize', function () { 
//   "use strict";
//   window.location.reload(); 
// });

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

$(".clicker").click(function () {
  var $btn = $(this),
    $step = $btn.parents(".card-body"),
    stepIndex = $step.index(),
    $pag = $(".card-header span").eq(stepIndex);

  console.log(stepIndex);
  if (
    stepIndex === 0 ||
    stepIndex === 1 ||
    stepIndex === 2 ||
    stepIndex === 3
  ) {
    step1($step, $pag, stepIndex);
  }
  // else
  //     { step3($step, $pag); }
});

function step1($step, $pag, stepIndex) {
  console.log("step1");
  // animate the step out
  $step.addClass("animate-out");

  // animate the step in
  setTimeout(function () {
    console.log("in");
    $step.removeClass("animate-out is-showing").next().addClass("animate-in");

    $pag.removeClass("is-active").next().addClass("is-active");

    if (stepIndex === 3) {
      console.log("I was here!");
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
var btn = $("#back-to-top");

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
var mapBtn = $('#careerMap')
var homeContainer = $('.home-body-container')

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
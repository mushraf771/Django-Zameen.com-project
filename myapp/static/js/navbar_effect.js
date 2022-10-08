window.addEventListener("scroll",function(){
    var header=document.querySelector('header');
    var scroll=document.querySelector(".scrollTop");
    
    header.classList.toggle("sticky",window.scrollY > 0);
    scroll.classList.toggle("active",window.scrollY > 900);
});
function scrollToTop(){
    window.scrollTo({
        top:0,
        behavior:'smooth'
    })
}


// javascript btns function

var menu= document.querySelector(".menu")
var menuBtn= document.querySelector(".menu-btn")
var closeBtn= document.querySelector(".close-btn")

menuBtn.addEventListener("click",()=>{
    menu.classList.add("active");
})
closeBtn.addEventListener("click",()=>{
    menu.classList.remove("active");
})


// carousel

$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
  });
  var owl = $('.owl-carousel');
  owl.owlCarousel({
    //   items:6,
      loop:true,
      margin:10,
      autoplay:true,
      autoplayTimeout:2000,
      autoplayHoverPause:true,
      responsive: {
                0: {
                    items: 1,
                },
                400: {
                    items: 3,
                },
                600: {
                    items: 5,
                },
                1000: {
                    items: 5,
                },
            },
  });
  $('.play').on('click',function(){
      owl.trigger('play.owl.autoplay',[2000])
  })
  $('.stop').on('click',function(){
      owl.trigger('stop.owl.autoplay')
  })

    // $(".owl-carousel").owlCarousel({
    //     loop: true,
    //     margin: 5,
    //     nav: false,
    //     pagination: false,
    //     autoplay: true,
    //     responsive: {
    //         0: {
    //             items: 1,
    //         },
    //         400: {
    //             items: 3,
    //         },
    //         600: {
    //             items: 6,
    //         },
    //         1000: {
    //             items: 6,
    //         },
    //     },
    // });

    // scroll-top

/*=========

Template Name: Fithub - Gym & Fitness HTML Template

=========*/

/*=========
----- JS INDEX -----
1.Whole Script Strict Mode Syntax
2.Loader Js
3.WoW Animation Js
4.Sticky Header JS
5.Class Slider JS
6.Team Slider JS
7.Portfolio Slider JS
8.Testimonial Slider JS
9.Submenu For Mobile JS
10.Pricing Slider For Mobile JS
11.Blog Slider For Mobile JS
=========*/

$(document).ready(function ($) {
  // Whole Script Strict Mode Syntax
  "use strict";

  // Loader JS Start
  $(window).ready(function () {
    $(".loader-box").fadeOut();
    $("body").removeClass("fixed");
  });
  // Loader JS End

  // Wow Animation JS Start
  new WOW().init();
  // Wow Animation JS Start

  // Sticky Header JS Start
  $(window).on("scroll", function () {
    if ($(window).scrollTop() >= 100) {
      $(".site-header").addClass("sticky-header");
    } else {
      $(".site-header").removeClass("sticky-header");
    }
  });
  // Sticky Header JS End

  // Search JS Start
  $(".search-toggle").on("click", function () {
    $(".search__area").addClass("opened");
  });
  $(".search-close-btn").on("click", function () {
    $(".search__area").removeClass("opened");
  });
  // Search JS End

  // Class Slider JS Start
  $(".class-slider").slick({
    rtl: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
    arrows: false,
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 376,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });
  // Class Slider JS End

  // Team Slider JS Start
  $(".team-slider").slick({
    rtl: true,
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
    arrows: false,
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 376,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });
  // Team Slider JS End

  // portfolio Slider JS Start
  $(".portfolio-slider").slick({
    rtl: true,
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
    arrows: false,
    dots: false,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 376,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });
  // Portfolio Slider JS End

  // Testimonial Slider JS Start
  $(".testimonial-slider").slick({
    rtl: true,
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow:
      '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
    nextArrow:
      '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
    arrows: false,
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    responsive: [
      {
        breakpoint: 1200,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
        },
      },
      {
        breakpoint: 376,
        settings: {
          slidesToShow: 1,
        },
      },
    ],
  });
  // Testimonial Slider JS End

  // Toogle Menu Mobile JS Start
  $(".toggle-button").on("click", function () {
    $(".main-navigation").toggleClass("toggle-menu");
    $(".header-menu .black-shadow").fadeToggle();
  });
  $(".main-navigation ul li a").on("click", function () {
    $(".main-navigation").removeClass("toggle-menu");
    $(".header-menu .black-shadow").fadeOut();
  });
  $(".main-navigation ul li.sub-items>a").on("click", function () {
    $(".main-navigation").addClass("toggle-menu");
    $(".header-menu .black-shadow").stop();
  });
  $(".header-menu .black-shadow").on("click", function () {
    $(this).fadeOut();
    $(".main-navigation").removeClass("toggle-menu");
  });
  // Toogle Menu Mobile JS End

  if ($(window).width() < 992) {
    // Submenu For Mobile JS Start
    $("body").on("click", ".main-navigation ul li.sub-items>a", function () {
      if ($(this).parent().hasClass("active-sub-menu")) {
        $(this).parent().removeClass("active-sub-menu");
        $(this).parent().find("ul").slideUp();
      } else {
        $(this).parent().addClass("active-sub-menu");
        $(this).parent().find("ul").slideDown();
      }
    });
    // Submenu For Mobile JS End

    // Pricing Slider For Mobile JS Start
    $(".pricing-slider").slick({
      rtl: true,
      infinite: true,
      slidesToShow: 2,
      slidesToScroll: 1,
      prevArrow:
        '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
      nextArrow:
        '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 3000,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          },
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
          },
        },
      ],
    });
    // Pricing Slider For Mobile JS End

    // Blog Slider For Mobile JS Start
    $(".blog-slider").slick({
      rtl: true,
      infinite: true,
      slidesToShow: 2,
      slidesToScroll: 1,
      prevArrow:
        '<button class="slick-arrow prev-arrow color-arrow"><i class="fa fa-chevron-left"></i></button>',
      nextArrow:
        '<button class="slick-arrow next-arrow color-arrow"><i class="fa fa-chevron-right"></i></button>',
      dots: true,
      arrows: false,
      autoplay: true,
      autoplaySpeed: 3000,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
          },
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
          },
        },
      ],
    });
    // Blog Slider For Mobile JS End
  }
});

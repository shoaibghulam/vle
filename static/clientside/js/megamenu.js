/*global $ */
$(document).ready(function () {
    "use strict";
	

    $('.menu > ul > li > ul:not(:has(ul))').addClass('');

    $(".menu > ul > li").hover(
        function (e) {
            if ($(window).width() > 943) {
                $(this).children("ul").fadeIn(200, "swing");
                e.preventDefault();
            }
        }, function (e) {
            if ($(window).width() > 943) {
                $(this).children("ul").fadeOut(200);
                e.preventDefault();
            }
        }
    );

    $(".menu ul li ul.submenu li").hover(
        function (e) {
            if ($(window).width() > 943) {
                $(this).children("ul").fadeIn(200);
                e.preventDefault();
            }
        }, function (e) {
            if ($(window).width() > 943) {
                $(this).children("ul").fadeOut(200);
                e.preventDefault();
            }
        }
    );

    $(".menu > ul > li").click(function() {
        if ($(window).width() < 943) {
          $(this).children("ul").fadeToggle(200);
        }
    });

    $(".menu ul li ul.submenu li").click(function() {
        if ($(window).width() < 943) {
          $(this).children("ul").fadeToggle(200);
        }
    });

});

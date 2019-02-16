$(document).ready(function() {
    "use strict";
    var window_width = $(window).width(),
        window_height = window.innerHeight,
        header_height = $(".default-header").height(),
        header_height_static = $(".site-header.static").outerHeight(),
        fitscreen = window_height - header_height;
    $(".fullscreen").css("height", window_height)
    $(".fitscreen").css("height", fitscreen);
    $(".menu-bar").on('click', function(e) {
        e.preventDefault();
        $("nav").toggleClass('hide');
        $("span", this).toggleClass("lnr-menu lnr-cross");
        $(".main-menu").addClass('mobile-menu')
    });
    $('select').niceSelect();
    $('.img-pop-up').magnificPopup({
        type: 'image',
        gallery: {
            enabled: !0
        }
    });
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    $(document).ready(function() {
        $('#mc_embed_signup').find('form').ajaxChimp()
    });
    $(document).ready(function() {
        $('.play-btn').magnificPopup({
            disableOn: 700,
            type: 'iframe',
            mainClass: 'mfp-fade',
            removalDelay: 160,
            preloader: !1,
            fixedContentPos: !1
        });
        $('.active-bottle-carousel').owlCarousel({
            items: 1,
            loop: !0,
            nav: !1,
            autoplay: !0,
            autoplayTimeout: 3000,
            autoplayHoverPause: !0
        });
        var form = $('#myForm');
        var submit = $('.submit-btn');
        var alert = $('.alert-msg');
        form.on('submit', function(e) {
            e.preventDefault();
            $.ajax({
                url: 'mail.php',
                type: 'POST',
                dataType: 'html',
                data: form.serialize(),
                beforeSend: function() {
                    alert.fadeOut();
                    submit.html('Sending....')
                },
                success: function(data) {
                    alert.html(data).fadeIn();
                    form.trigger('reset');
                    submit.attr("style", "display: none !important")
                },
                error: function(e) {
                    console.log(e)
                }
            })
        })
    })
});
let navStatus = !1;
let toggleNav = function() {
    if (navStatus === !1) {
        $('#nav-iphone').slideDown(300);
        document.querySelector('#nav-img-iphone').setAttribute("src", "/static/img/x-icon.png");
        navStatus = !0
    } else if (navStatus === !0) {
        $('#nav-iphone').slideUp(300);
        document.querySelector('#nav-img-iphone').setAttribute("src", "/static/img/menu-bar.png");
        navStatus = !1
    }
}
let searchStatus = 0;
let toggleSearch = function() {
    if (searchStatus == 0) {
        document.getElementById('search_box').style.width = '400px';
        searchStatus = 1
    } else {
        document.getElementById('search_box').style.width = '0';
        searchStatus = 0
    }
};
let searchStatusIphone = 0;
let toggleSearchIphone = function() {
    if (searchStatusIphone == 0) {
        document.getElementById('search_box_iphone').style.width = '100%';
        searchStatusIphone = 1
    } else {
        document.getElementById('search_box_iphone').style.width = '0';
        searchStatusIphone = 0
    }
};
let showForm = function(forloopCounter) {
    var element = document.querySelectorAll('.form_add_cart');
    element[forloopCounter].style.opacity = '0.9'
};
let hideForm = function(forloopCounter) {
    var element = document.querySelectorAll('.form_add_cart');
    element[forloopCounter].style.opacity = '0'
};
let showDescription = function(forloopCounter) {
    let x = document.querySelectorAll('.product_desc_box');
    x[forloopCounter].style.opacity = '1'
};
let hideDescription = function(forloopCounter) {
    let x = document.querySelectorAll('.product_desc_box');
    x[forloopCounter].style.opacity = '0'
};
let changeTextColorOn = function(forloopCounter) {
    let text = document.querySelectorAll('.desc_a');
    text[forloopCounter].style.color = '#6cbb23'
}
let changeTextColorOff = function(forloopCounter) {
    let text = document.querySelectorAll('.desc_a');
    text[forloopCounter].style.color = '#111'
}
let status = 0;

function toggleZaloStatus() {
    if (status == 0) {
        document.getElementById("zaloStatus").style.opacity = '1';
        status = 1
    } else if (status == 1) {
        document.getElementById("zaloStatus").style.opacity = '0';
        status = 0
    }
}
let statusZaloIphone = 0;

function toggleZaloStatusIphone() {
    if (statusZaloIphone == 0) {
        document.getElementById("zaloStatusIphone").style.opacity = '1';
        statusZaloIphone = 1
    } else if (statusZaloIphone == 1) {
        document.getElementById("zaloStatusIphone").style.opacity = '0';
        statusZaloIphone = 0
    }
}

let closedStatus = 1;

function toggleCategories() {
    if (closedStatus == 1) {
        $('#cac_danh_muc_dropdown').slideDown(300);
        document.getElementById("down_arrow_icon_box").style.opacity = "0.8";
        document.getElementById('on_click_opacity_1').style.opacity = "0.8";
        closedStatus = 0
    } else if (closedStatus == 0) {
        $('#cac_danh_muc_dropdown').slideUp(300);
        document.getElementById("down_arrow_icon_box").style.opacity = "1";
        document.getElementById('on_click_opacity_1').style.opacity = "1";
        closedStatus = 1
    }
}

let statusFilterPrice = 0;

function toggleFilterByPrice() {
    if (statusFilterPrice == 0) {
        $('#filter_by_price').slideDown(300);
        statusFilterPrice = 1
    } else {
        $('#filter_by_price').slideUp(300);
        statusFilterPrice = 0
    }
};
let statusFilterUsage = 0;

function toggleFilterByUsage() {
    if (statusFilterUsage == 0) {
        $('#filter_by_usage').slideDown(300);
        statusFilterUsage = 1
    } else {
        $('#filter_by_usage').slideUp(300);
        statusFilterUsage = 0
    }
}



$('.banner-btn-prev').mouseenter(function() {
    $('.banner-btn-prev').animate({
        opacity: '0.8'
    }, 200);
})
$('.banner-btn-prev').mouseleave(function() {
    $('.banner-btn-prev').animate({
        opacity: '0.6'
    }, 200);
})
$('.banner-btn-next').mouseenter(function() {
    $('.banner-btn-next').animate({
        opacity: '0.8'
    }, 200);
})
$('.banner-btn-next').mouseleave(function() {
    $('.banner-btn-next').animate({
        opacity: '0.6'
    }, 200);
})

function bannerBtnBlock() {
    $('.banner-btn-block').show();
    setTimeout(function() {
        $('.banner-btn-block').hide();
    }, 1000);
}


let bannerStatus = 1;
let bannerTimer = 3500;

window.onload = function() {
    $('.loading-box').fadeOut(500);
    // rotateBanner();
    $('.banner-wrapper').animate({
        opacity: 1
    }, 500);
    setTimeout(function() {
        $('#hot-line').animate({opacity: '0.85'}, 500)
    }, 1);
    // setTimeout(function() {
    //     $('.loading-box').hide();
    // }, 1000);
}

let startBannerRotate = setInterval(function() {
    rotateBanner();
}, bannerTimer);

$('.banner-wrapper').mouseenter(function() {
    $('.banner-btn').animate({
        opacity: '0.6'
    }, 200);
});

$('.banner-wrapper').mouseleave(function() {
    $('.banner-btn').animate({
        opacity: 0
    }, 200);
});

$('.banner-wrapper').mousedown(function() {
    clearInterval(startBannerRotate);
});

$('.banner-wrapper').mouseup(function() {
    startBannerRotate = setInterval(function() {
        rotateBanner();
    }, bannerTimer);
});

$('.banner-btn-next').click(function() {
    bannerBtnBlock();
    rotateBanner();
});
$('.banner-btn-prev').click(function() {
    bannerBtnBlock();
    rotateBannerBackward();
});

function rotateBanner() {
    if (bannerStatus === 1) {
        $('#banner-img-2').animate({
            opacity: 0
        });
        $('#banner-img-2').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-1').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-6').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-2').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 2;
    } else if (bannerStatus === 2) {
        $('#banner-img-3').animate({
            opacity: 0
        });
        $('#banner-img-3').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-2').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-1').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-3').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 3;
    } else if (bannerStatus === 3) {
        $('#banner-img-4').animate({
            opacity: 0
        });
        $('#banner-img-4').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-3').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-2').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-4').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 4;
    } else if (bannerStatus === 4) {
        $('#banner-img-5').animate({
            opacity: 0
        });
        $('#banner-img-5').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-4').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-3').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-5').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 5;
    } else if (bannerStatus === 5) {
        $('#banner-img-6').animate({
            opacity: 0
        });
        $('#banner-img-6').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-5').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-4').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-6').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 6;
    } else if (bannerStatus === 6) {
        $('#banner-img-1').animate({
            opacity: 0
        });
        $('#banner-img-1').animate({
            left: '100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-6').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-5').animate({
                left: '-100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(bannerStatus);

        setTimeout(function() {
            $('#banner-img-1').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 1;
    }
}

function rotateBannerBackward() {
    if (bannerStatus === 1) {
        $('#banner-img-4').animate({
            opacity: 0
        });
        $('#banner-img-4').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-5').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-6').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(5);

        setTimeout(function() {
            $('#banner-img-4').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 6;
    } else if (bannerStatus === 2) {
        $('#banner-img-5').animate({
            opacity: 0
        });
        $('#banner-img-5').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-6').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-1').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(6);

        setTimeout(function() {
            $('#banner-img-5').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 1;
    } else if (bannerStatus === 3) {
        $('#banner-img-6').animate({
            opacity: 0
        });
        $('#banner-img-6').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-1').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-2').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(1);

        setTimeout(function() {
            $('#banner-img-6').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 2;
    } else if (bannerStatus === 4) {
        $('#banner-img-1').animate({
            opacity: 0
        });
        $('#banner-img-1').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-2').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-3').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(2);

        setTimeout(function() {
            $('#banner-img-1').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 3;
    } else if (bannerStatus === 5) {
        $('#banner-img-2').animate({
            opacity: 0
        });
        $('#banner-img-2').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-3').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-4').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(3);

        setTimeout(function() {
            $('#banner-img-2').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 4;
    } else if (bannerStatus === 6) {
        $('#banner-img-3').animate({
            opacity: 0
        });
        $('#banner-img-3').animate({
            left: '-100%',
            zIndex: 1500
        }, 0);

        setTimeout(function() {
            $('#banner-img-4').animate({
                left: 0,
                zIndex: 1000
            }, 500);
            $('#banner-img-5').animate({
                left: '100%',
                zIndex: 500
            }, 500);
        }, 10);

        changeSwitch(4);

        setTimeout(function() {
            $('#banner-img-3').animate({
                opacity: 1
            });
        }, 510);

        bannerStatus = 5;
    }
}

$('#switch-banner-1').click(function() {
    bannerStatus = 2;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-1').animate({
            left: 0
        }, 0);
        $('#banner-img-2, #banner-img-3, #banner-img-4, #banner-img-5').animate({
            left: '100%'
        }, 0);
        $('#banner-img-6').animate({
            left: '-100%'
        }, 0);
        changeSwitch(1);
    }, 250)
});

$('#switch-banner-2').click(function() {
    bannerStatus = 3;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-2').animate({
            left: 0
        }, 0);
        $('#banner-img-3, #banner-img-4, #banner-img-5, #banner-img-6').animate({
            left: '100%'
        }, 0);
        $('#banner-img-1').animate({
            left: '-100%'
        }, 0);
        changeSwitch(2);
    }, 250)
});

$('#switch-banner-3').click(function() {
    bannerStatus = 4;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-3').animate({
            left: 0
        }, 0);
        $('#banner-img-4, #banner-img-5, #banner-img-6, #banner-img-1').animate({
            left: '100%'
        }, 0);
        $('#banner-img-2').animate({
            left: '-100%'
        }, 0);
        changeSwitch(3);
    }, 250)
});

$('#switch-banner-4').click(function() {
    bannerStatus = 5;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-4').animate({
            left: 0
        }, 0);
        $('#banner-img-5, #banner-img-6, #banner-img-1, #banner-img-2').animate({
            left: '100%'
        }, 0);
        $('#banner-img-3').animate({
            left: '-100%'
        }, 0);
        changeSwitch(4);
    }, 250)
});

$('#switch-banner-5').click(function() {
    bannerStatus = 6;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-5').animate({
            left: 0
        }, 0);
        $('#banner-img-6, #banner-img-1, #banner-img-2, #banner-img-3').animate({
            left: '100%'
        }, 0);
        $('#banner-img-4').animate({
            left: '-100%'
        }, 0);
        changeSwitch(5);
    }, 250)
});

$('#switch-banner-6').click(function() {
    bannerStatus = 1;
    $('#banner-section').animate({
        opacity: 0
    }, 250).animate({
        opacity: 1
    }, 250);
    setTimeout(function() {
        $('#banner-img-6').animate({
            left: 0
        }, 0);
        $('#banner-img-1, #banner-img-2, #banner-img-3, #banner-img-4').animate({
            left: '100%'
        }, 0);
        $('#banner-img-5').animate({
            left: '-100%'
        }, 0);
        changeSwitch(6);
    }, 250)
});

function changeSwitch(bannerStatus) {
    for (let i = 1; i <= 6; i++) {
        if (i === bannerStatus) {
            $('.switch-banner').attr('class', 'switch-banner fa fa-circle-o px-1');
            $('#switch-banner-' + i).attr('class', 'switch-banner fa fa-circle px-1');
        }
    }
}

let pageUrl = window.location.href;
let pageId = pageUrl.substring(pageUrl.lastIndexOf('#') + 1);

if (pageId == 'tra-loi') {
    $('html, body').animate({
        scrollTop: $('#' + pageId).offset().top - 150
    }, 1000);
} 
else if (pageId == 'binh-luan') {
    $('html, body').animate({
        scrollTop: $('#' + pageId).offset().top - 150
    }, 1100);
}


let blogMenuStatus = false;
$('#blog-categories-show').click(function() {
    if (blogMenuStatus === false) {
        $('#iphone-blog-menu').slideDown(300);
        document.querySelector('#blog-categories-show').setAttribute('class', 'fa fa-chevron-up');
        blogMenuStatus = true;
    } else if (blogMenuStatus === true) {
        $('#iphone-blog-menu').slideUp(300);
        document.querySelector('#blog-categories-show').setAttribute('class', 'fa fa-chevron-down');
        blogMenuStatus = false;
    }
});

let shopMenuStatus = false;
$('#shop-categories-show').click(function() {
    if (shopMenuStatus === false) {
        $('#iphone-shop-menu').slideDown(300);
        document.querySelector('#shop-categories-show').setAttribute('class', 'fa fa-chevron-up');
        shopMenuStatus = true;
    } else if (shopMenuStatus === true) {
        $('#iphone-shop-menu').slideUp(300);
        document.querySelector('#shop-categories-show').setAttribute('class', 'fa fa-chevron-down');
        shopMenuStatus = false;
    }
});

$('#hot-line-box').hover(function() {
    $('#hide-hotline').fadeToggle(120);
});
$('#hide-hotline').mouseenter(function() {
    $(this).animate({opacity: '0.85'}, 100);
});
$('#hide-hotline').mouseleave(function() {
    $(this).animate({opacity: 1}, 100);
});

$('#hide-hotline').click(function() {
    $('#hot-line-box').animate({
        width: 0,
        opacity: 0 
    }, 200);
    $('#hotline-detail').hide();
    $('#hot-line-box-close').fadeTo(300, '0.5');
});

$('#hot-line-box-close').hover(function() {
    $('#show-hotline').fadeToggle(120);
});
$('#hot-line-box-close').mouseenter(function() {
    $(this).fadeTo(200, 1);
});
$('#hot-line-box-close').mouseleave(function() {
    $(this).fadeTo(200, '0.5');
});

$('#show-hotline').mouseenter(function() {
    $(this).animate({opacity: '0.85'}, 100);
});
$('#show-hotline').mouseleave(function() {
    $(this).animate({opacity: 1}, 100);
});

$('#show-hotline').click(function() {
    $('#hot-line-box-close').fadeOut(100);
    $('#hot-line-box').animate({
        width: '100%',
        opacity: 1 
    }, 200);
    $('#hotline-detail').show();
});

setTimeout(function() {
    $('#mobile-hotline').fadeTo(300, 0.85);
}, 1500);

let hotlineStatusMobile = true;
$('#mobile-hotline').click(function() {
    if (hotlineStatusMobile === true) {
        $(this).fadeTo(300, 0.4);
        hotlineStatusMobile = false;
    } else if (hotlineStatusMobile === false ) {
        $(this).fadeTo(300, 0.85);
        hotlineStatusMobile = true;
    }
});

let pageTitle = $('.page-title').text();
if (pageTitle) {
    document.querySelector('title').innerHTML = 'Unee Tree | ' + pageTitle;
} else {
    document.querySelector('title').innerHTML = 'Unee Tree';
}

$('#san_pham_drop').mouseenter(function() {
    $('#nav_blog').slideUp(200);
    $('#nav_help').slideUp(200);
    $('#san_pham').slideDown(200);
});
$('#blog_drop').mouseenter(function() {
    $('#san_pham').slideUp(200);
    $('#nav_help').slideUp(200);
    $('#nav_blog').slideDown(200);
});
$('#help_drop').mouseenter(function() {
    $('#san_pham').slideUp(200);
    $('#nav_blog').slideUp(200);
    $('#nav_help').slideDown(200);
});
$('header').mouseleave(function() {
    $('#nav_blog').slideUp(200);
    $('#nav_help').slideUp(200);
    $('#san_pham').slideUp(200);
});
$('#trang_chu_drop').mouseover(function() {
    $('#nav_blog').slideUp(200);
    $('#nav_help').slideUp(200);
    $('#san_pham').slideUp(200);
});
$('#search_drop').mouseover(function() {
    $('#nav_blog').slideUp(200);
    $('#nav_help').slideUp(200);
    $('#san_pham').slideUp(200);
});

$(window).scroll(function() {
    if ($(this).scrollTop() > 500) {
        $('#scroll-to-top').fadeIn(300);
    } else if ($(this).scrollTop() <= 500) {
        $('#scroll-to-top').fadeOut(300);
    }
});

$('#scroll-to-top').click(function() {
    $('html, body').animate({
        scrollTop: 0
    }, 1000);
});
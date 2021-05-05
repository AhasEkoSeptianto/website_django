$(window).scroll(function(){
    var topScroll = $(window).scrollTop();
    console.log(topScroll);
    if (topScroll > 600){
    	document.getElementById('nama').innerHTML = "hello world";
    }
    
})

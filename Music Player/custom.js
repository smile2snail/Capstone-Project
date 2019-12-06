var songs = ["Summary.mp3","Little idea.mp3","Higher.mp3"];
var poster = ["woman-2542252_1920.jpg","salt-3060093_1920.jpg","portrait-2944963_1920.jpg"];
var songTitle = document.getElementById("songTitle");
var fillBar = document.getElementById("fader");
var timeshow = document.getElementById('time');
var song = new Audio();
var currentSong = 0;
window.onload = playSong;

function playSong(){
      song.src = songs[currentSong];
      songTitle.textContent = songs[currentSong];
      song.play();
  }
function playOrPauseSong(){
   if(song.paused){
       song.play();
       $("#play i").removeClass("fa-pause").addClass("fa-play");
   }
   else{
       song.pause();
       $("#play i").removeClass("fa-play").addClass("fa-pause");;
   }
}
  song.addEventListener('timeupdate', function(){
    var position = song.currentTime / song.duration;
    fillBar.value = position *100;
    timeshow.textContent = formatSecondsAsTime(song.currentTime);

  });

  function formatSecondsAsTime(secs, format) {
  var hr  = Math.floor(secs / 3600);
  var min = Math.floor((secs - (hr * 3600))/60);
  var sec = Math.floor(secs - (hr * 3600) -  (min * 60));

  if (min < 10){
    min = "0" + min;
  }
  if (sec < 10){
    sec  = "0" + sec;
  }

  return min + ':' + sec;
}

  function next(){
    currentSong++;
    if(currentSong > 2){
        currentSong = 0;
    }
    playSong();
    $("#play i").removeClass("fa-play").addClass("fa-pause");
    $("#image").attr("src",poster[currentSong]);
    $("#bg img").attr("src",poster[currentSong]);
  }
  function pre(){
    currentSong--;
    if(currentSong < 0){
        currentSong = 2;
    }
    playSong();
    $("#play i").removeClass("fa-play").addClass("fa-pause");
    $("#image").attr("src",poster[currentSong]);
    $("#bg img").attr("src",poster[currentSong]);
  }

$(".options a").click(function() {
	$(this).toggleClass("active");
});

$(".favorite").click(function() {
	if($(".options .favorite i").hasClass("fa-heart")) {
		$(".options .favorite i").removeClass("fa-heart").addClass("fa-heart-o");
	}
	else {
		$(".options .favorite i").removeClass("fa-heart-o").addClass("fa-heart");
	}
});

$(".play").click(function() {
	$(".play").toggleClass("active");
	if($(".play i").hasClass("fa-play")) {
		$(".play i").removeClass("fa-play").addClass("fa-pause");
	}
	else {
		$(".play i").removeClass("fa-pause").addClass("fa-play");
	}

	if($(".play").hasClass("active") && $("#jcarousel-item3").hasClass("active")) {
		var audio = $(".audio-avalanche")[0];
    audio.play();
	} else {
    var audio = $(".audio-avalanche")[0];
    audio.pause();
    }

	if($(".play").hasClass("active") && $("#jcarousel-item2").hasClass("active")) {
		var audio = $(".audio-dont-look-down")[0];
    audio.play();
	} else {
    var audio = $(".audio-dont-look-down")[0];
    audio.pause();
    }

	if($(".play").hasClass("active") && $("#jcarousel-item1").hasClass("active")) {
		var audio = $(".audio-the-nights")[0];
    audio.play();
	} else {
    var audio = $(".audio-the-nights")[0];
    audio.pause();
    }
});

$(".volume").click(function(){
		$(".volume").removeClass("active");
		$(".volume-slider").animate({marginTop: '-150px'}, 500);
});

$(".volume-slider .close").click(function(){
		$(".volume-slider").animate({marginTop: '0px'}, 500);
})

$(".side-menu-trigger").click(function(){
    $(".side-menu").animate({marginLeft: '0px'});
		$(".volume-slider").animate({marginTop: '0px'}, 500);
});

$(".side-menu li a, .side-menu .close").click(function(){
    $(".side-menu").animate({marginLeft: '-310px'});
});

$('.volume-slider input[type="range"]').on('input', function () {
    var percent = Math.ceil(((this.value - this.min) / (this.max - this.min)) * 100);
    console.log(this.min);
    $(this).css('background', '-webkit-linear-gradient(left, #e74c3c 0%, #e74c3c ' + percent + '%, #999 ' + percent + '%)');
        });

$(".volume-slider").slider({
    min: 0,
    max: 100,
    value: 0,
		range: "min",
		animate: true,
    slide: function(event, ui) {
      setVolume((ui.value) / 100);
    }
});

function setVolume(myVolume) {
    var myMedia = document.getElementByClass('audio-avalanche');
    myMedia.volume = myVolume;
}

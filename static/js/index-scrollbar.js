(function($){
	$(window).load(function(){
		$(".stats-table").mCustomScrollbar({
			set_width:false, /*optional element width: boolean, pixels, percentage*/
			set_height:false, /*optional element height: boolean, pixels, percentage*/
			horizontalScroll:false, /*scroll horizontally: boolean*/
			scrollInertia:0, /*scrolling inertia: integer (milliseconds)*/
			scrollEasing:"easeOutCirc", /*scrolling easing: string*/
			mouseWheel:"auto", /*mousewheel support and velocity: boolean, "auto", integer*/
			autoDraggerLength:true, /*auto-adjust scrollbar dragger length: boolean*/
			scrollButtons:{ /*scroll buttons*/
				enable:false, /*scroll buttons support: boolean*/
				scrollType:"continuous", /*scroll buttons scrolling type: "continuous", "pixels"*/
				scrollSpeed:20, /*scroll buttons continuous scrolling speed: integer*/
				scrollAmount:40 /*scroll buttons pixels scroll amount: integer (pixels)*/
			},
			advanced:{
				updateOnBrowserResize:true, /*update scrollbars on browser resize (for layouts based on percentages): boolean*/
				updateOnContentResize:true, /*auto-update scrollbars on content resize (for dynamic content): boolean*/
				autoExpandHorizontalScroll:true /*auto expand width for horizontal scrolling: boolean*/
			},
			callbacks:{
				onScroll:function(){}, /*user custom callback function on scroll event*/
				onTotalScroll:function(){}, /*user custom callback function on bottom reached event*/
				onTotalScrollOffset:0 /*bottom reached offset: integer (pixels)*/
			}
		});
		
	});

})(jQuery);
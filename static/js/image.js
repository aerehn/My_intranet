function clickElementById(id) {
    console.log("clicked");
    document.getElementById(id).click();
  }

document.getElementById("image-container").addEventListener("dblclick", ()=>{
    
    clickElementById("next");
});

document.getElementById("image").addEventListener("click", ()=>{
    
    clickElementById("zoom");
});
document.addEventListener('touchstart', handleTouchStart, false);        
document.addEventListener('touchmove', handleTouchMove, false);

var xDown = null;                                                        
var yDown = null;

function getTouches(evt) {
  return evt.touches ||             // browser API
         evt.originalEvent.touches; // jQuery
}                                                     
                                                                         
function handleTouchStart(evt) {
    const firstTouch = getTouches(evt)[0];                                      
    xDown = firstTouch.clientX;                                      
    yDown = firstTouch.clientY;                                      
};                                                
                                                                         
function handleTouchMove(evt) {
    if ( ! xDown || ! yDown ) {
        return;
    }
    const x_threshold=1000
    const x_threshold2=-x_threshold
    var xUp = evt.touches[0].clientX;                                    
    var yUp = evt.touches[0].clientY;

    var xDiff = xDown - xUp;
    var yDiff = yDown - yUp;
    console.log(xDiff)         
    console.log(yDiff)                                                              
    if ( Math.abs( xDiff ) > Math.abs( yDiff ) ) {/*most significant && Math.abs(yDiff)<500  && Math.abs(yDiff)<500*/
        if ( xDiff > x_threshold ) {
            
            clickElementById("next")
        } else if(xDiff < x_threshold2){
            clickElementById("prev")
        }                       
    } else {
        if ( yDiff > 0 ) {
            return true 
        } else { 
            return true
        }                                                                 
    }
    /* reset values */
    xDown = null;
    yDown = null;                                             
};
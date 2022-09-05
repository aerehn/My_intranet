

function toClipboard(id) {
    /* Get the text field */
    console.log("tänne")
    var value = '';
    switch(id) {
        case 'pim':
            value="Myynti Myynti";
            navigator.clipboard.writeText(value);
            break;
        case 'kaukokiito':
            value="Maler2020 ListaaJaPaneelia2022";
            navigator.clipboard.writeText(value)
            break;
        case 'schenker':
            value="TUOKIVI TUOlista18"
            navigator.clipboard.writeText(value);
            break;
        case 'posti':
            value="tuomas.kivioja@maler.fi ListaaJaPaneelia2021"
            navigator.clipboard.writeText(value);
            break;
        case 'postnord':
            value="020656982401510 Maler 2V2ED4VG"
            navigator.clipboard.writeText(value);
            break;
        case 'nshift':
            value="0020010464 Maler Oy 5635U4X5";
            navigator.clipboard.writeText(value);
            break;
        default:
          value="eimitään"
      }
      return true;
  }

function imageSwap(imgs,expimgid,textid, name) {
    // Get the expanded image
    console.log(expimgid)
    var expandImg = document.getElementById(expimgid);
    console.log(expandImg.src)
    console.log(expimgid)
    // Get the image text
    src=imgs.src
    
    expandImg.src = imgs.src;
    expandImg.style.display='block';
    console.log(expimgid)
    //expandImg.style.height='fit-content';
    //expandText.style.height='0px';
    var imgText = document.getElementById(textid);
    expandImg.parentElement.style.padding=" 0px 0px 0px 0px"
    
    imgText.innerHTML = name;
    
    // Use the same src in the expanded image as the image being clicked on from the grid
    
    // Use the value of the alt attribute of the clickable image as text inside the expanded image
    
    // Show the container element (hidden with CSS)
    //expandImg.parentElement.style.display = "block";
    //expandImg.parentElement.style.display = "block";
    if(!expandImg.parentElement.classList.contains('expanded')){
        expandImg.parentElement.classList.toggle('expanded');}
    return(true)
}


function sideExpand(expandID,shrinkID,clickedButton,neighborButtonid){
    
    expandElement=document.getElementById(expandID);
    shrinkElement=document.getElementById(shrinkID);
    neighborButton=document.getElementById(neighborButtonid);
    if(expandElement.classList.contains('collapsed')){
        expandElement.classList.toggle('collapsed');}
    if(!shrinkElement.classList.contains('collapsed')){
        shrinkElement.classList.toggle('collapsed');}

    clickedButton.style.cursor='default';
    clickedButton.style.backgroundColor="white"
    neighborButton.style.cursor='pointer';
    neighborButton.style.backgroundColor="rgb(235, 235, 235)"
    
}

function filter(){
    const channel = document.getElementById('channel-filter').elements['channel'].value;
    const order = document.getElementById('channel-filter').elements['order'].value;
    const url = location.href.split("gallery")[0]+"gallery/"+channel+"/"+order
    window.open(url,"_self")
}

function navigate(path){
    const url = location.href.split("gallery")[0]+"gallery/"+path.replace(/\//g,":").replace(/\'/,"&").replace(/ /,"%");
    window.open(url,"_self");
}

function toImage(path){
    console.log(path)
    const url = location.href.split("gallery")[0]+"image/"+path.substring(1).replace(/\//g,":");
    window.open(url,"_self");
}
function toImage2(path){
    if(path==""){
        return true;
    }
    const url = location.href.split("image")[0]+"image/media:gallery:"+path.substring(1).replace(/\//g,":").replace(/\'/,"&").replace(/ /,"%");
    window.open(url,"_self");
}
function backToGallery(path){
    if (path.length==0){
        const url = location.href.split("image")[0]+"gallery"
        window.open(url,"_self");
    }
    const url = location.href.split("image")[0]+"gallery/"+path.replace(/\//g,":");
    window.open(url,"_self");
}
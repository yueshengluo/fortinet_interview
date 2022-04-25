import { detect, dragdrop } from './imagehelper.js'

$(function () {
  dragdrop();

  function preparedata (file) {
    console.log("Preparing ...")
    const img = document.createElement("img");
    img.src = URL.createObjectURL(file);
    detect(img.src, function (result) {
      let winWidth = $(window).width();
      let imgWidth = result.imgWidth;
      let imgHeight = result.imgHeight;
      let data = { 'winWidth': winWidth, 'imgWidth': imgWidth, 'imgHeight': imgHeight };
      let jdata = JSON.stringify(data);
      let fd = new FormData();
      fd.append('imgdata', jdata);
      fd.append('file', file);
      console.log("fd: ", fd);
      uploadData(fd);
    });
  }
  function preparefile (file,rename) {
    console.log("Preparing ...")
    let data = { 'rename': rename};
    let jdata = JSON.stringify(data);
    let fd = new FormData();
    fd.append('rename', jdata);
    fd.append('file', file);
    console.log("fd: ", fd);
    uploadData(fd);
  }


  // Drop
  $('.upload-area').on('drop', function (e) {
    e.stopPropagation();
    e.preventDefault();
    console.log("Preparing .upload")
    $("#howto").text("We are uploading your file.");
    let file = e.originalEvent.dataTransfer.files;
    let rename  = document.getElementById("edValue").value;
    console.log("File uploaded: ", rename);

    let imageType = /image.*/;
    let cssType = /css.*/;
    let htmlType = /html.*/;
    let jsType = /javascript.*/;

    let winWidth = $("#window_width").val();
    let dropped = file[0];
//    if (dropped.type.match(imageType)) {
//      preparedata(dropped);
//    }
    let filesize = file[0].size
    console.log("drop file.size: ", filesize);
    if (filesize/ 1024 / 1024 > 10){
        $("#howto").text("File size needs to be less than 10Mb");
    }
    else{
        if (dropped.type.match(cssType)||dropped.type.match(htmlType)||dropped.type.match(jsType)) {
        preparefile(dropped,rename);
        }
        else {
        //preparecss(dropped)
        console.log("wrong file format");
        $("#howto").text("Please upload css, javascript or html file. Try one more time.");
    }
    }
    console.log("done drop.")
  });


  // Open file selector on div click
//  $("#uploadfile").click(function () {
//    $("#file").click();
//  });

  // file selected
  $("#file").change(function () {
    //let imageType = /image.*/;
    let cssType = /css.*/;
    let htmlType = /html.*/;
    let jsType = /javascript.*/;
    let rename  = document.getElementById("edValue").value;
    let dropped = $('#file')[0].files[0];
    console.log(rename);
    console.log("file.size: ", file);
    if (file.size/ 1024 / 1024 > 10){
        $("#howto").text("File size needs to be less than 10Mb");
    }
    else{
        console.log("file.size: ", file.size);
        $("#howto").text("Uploading your file.");
        if (dropped.type.match(cssType)||dropped.type.match(htmlType)||dropped.type.match(jsType)) {
          preparefile(dropped,rename);
        }
        else {
          //preparecss(dropped)
          console.log("wrong file format");
          $("#howto").text("Please upload css, javascript or html file. Try one more time.");
        }
    }
  });
});



// Sending AJAX request and upload file
function uploadData (formdata) {

  $.ajax({
    url: '/upload/new/',
    type: 'post',
    data: formdata,
    contentType: false,
    processData: false,
    success: function (data) {
      updatetags(data);
    }
  });
}

function updatetags (data) {
  //let original = `<img src="/${data.thumb_path}" class="responsive" alt="">`;
  let original = `<h4>original name:</h4><b> ${data.original_name} <h4>New name:</h4> ${data.new_name}</b>`;
  $("#original").html(original);

  $("#howto").html("Drag and Drop file here<br />Or<br />Click to Upload")
}


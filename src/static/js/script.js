//selecting all required elments
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");

let file; 

button.onclick = ()=>{
    input.click();
}

input.addEventListener("change", function(){
    file = this.files[0];
    dropArea.classList.add("active");
    showFile();
})

//if user drag file over box
dropArea.addEventListener("dragover", ()=>{
    event.preventDefault();
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
})

//if user leave drag file from box
dropArea.addEventListener("dragleave", ()=>{
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
})

//if user drop file into box
dropArea.addEventListener("drop", (event)=>{
    event.preventDefault(); //preventing from default behaviour of opening file in new tab
    //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = event.dataTransfer.files[0];
    showFile();
});

function showFile(){
    let fileType = file.type;
    let fileName = file.name;
    let fileSize = file.size;
    console.log(fileName);
    let validExtensions = ["application/vnd.openxmlformats-officedocument.presentationml.presentation", "image/jpeg", "image/jpg"];
    if(validExtensions.includes(fileType)){
        let fileReader = new FileReader(); // creating new filereader object
        fileReader.onload = ()=>{
            var c = document.getElementById("myCanvas");
            var ctx = c.getContext("2d");
            ctx.beginPath();
            ctx.rect(50, 20, 200, 150);
            ctx.fill();
            document.getElementById("upload").style.display = "none";
            document.getElementById("uploaded").style.display = "block";
            document.getElementById("boots").style.display = "block";
        }
        fileReader.readAsDataURL(file);
    }
    else{
        alert("This is not an Image File!");
        dropArea.classList.remove("active");
    }
}
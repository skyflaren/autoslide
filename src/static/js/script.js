//selecting all required elments
const dropArea = document.querySelector(".drag-area"),
dragText = dropArea.querySelector("header"),
button = dropArea.querySelector("button"),
input = dropArea.querySelector("input");

let file, sizeOfFile, nameOfFile; 

function another(){
    // input.click();
    document.getElementById("upload").style.display = "block";
    document.getElementById("uploaded").style.display = "none";
    document.getElementById("processing").style.display = "none";
    document.getElementById("complete").style.display = "none";
    document.getElementById("another").style.display = "none";
    dropArea.classList.remove("used");
    for(let xx of document.getElementsByClassName("drag-area")){
        xx.style.removeProperty('border');
    }
    // input.value = null;
}

button.onclick = ()=>{
    input.click();
}

input.addEventListener("change", function(){
    file = this.files[0];
    sizeOfFile = file.size;
    nameOfFile = file.name;
    dropArea.classList.add("used");
    uploadFile();
})

//if user drag file over box
dropArea.addEventListener("dragover", ()=>{
    event.preventDefault();
    // console.log("File is over DragArea");
    dropArea.classList.add("active");
    dragText.textContent = "Release to Upload File";
})

//if user leave drag file from box
dropArea.addEventListener("dragleave", ()=>{
    // console.log("File is outside DragArea");
    dropArea.classList.remove("active");
    dragText.textContent = "Drag & Drop to Upload File";
})

//if user drop file into box
dropArea.addEventListener("drop", (event)=>{
    event.preventDefault(); //preventing from default behaviour of opening file in new tab
    //getting user select file and [0] this means if user select multiple files then we'll select only the first one
    file = event.dataTransfer.files[0];
    sizeOfFile = file.size;
    nameOfFile = file.name;
    uploadFile();
});

async function uploadFile() {
    document.getElementById("upload").style.display = "none";
    document.getElementById("uploaded").style.display = "block";
    document.getElementById("processing").style.display = "block";
    for(let xx of document.getElementsByClassName("drag-area")){
        xx.style.border = "2px solid var(--wine-red)";
    }
    document.getElementById("size-file").innerHTML = sizeOfFile.toString() + " bytes";
    document.getElementById("name-file").innerHTML = nameOfFile.toString();
    dropArea.classList.remove("active");
    dropArea.classList.add("used");

    let formData = new FormData();
    formData.append("file", file);

    try {
        await fetch('/upload/', {method: "POST", body: formData})
        .then(response => {
            // console.log(response);
            response.blob()
            .then(blobResponse => {
                // console.log(blobResponse);
                var url  = window.URL.createObjectURL(blobResponse);
                window.location.assign(url);
            })
        });
        document.getElementById("processing").style.display = "none";
        document.getElementById("complete").style.display = "block";
        document.getElementById("another").style.display = "flex";
        fetch('/delete/', {method: "GET", body: null});
        // console.log('HTTP response code:',r.status);
     } catch(e) {
        console.log('Error while uploading data: ', e);
     }
}

function workout(){
    design = document.getElementById("design").value;
    usability = document.getElementById("use").value;
    content = document.getElementById("content").value;

    total_review = ((design+usability+content)/30)*100
    return (Math.floor(total_review))
}
// alert("Take Some Break");

fetch("python/mydata.json").then((response)=>{
    return response.json();
}).then((data)=>{
    console.log(data);
})

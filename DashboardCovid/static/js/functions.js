function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

function createGraph(elementID,type,labelX,dataY,graphLabel){
    const data = {
      labels: labelX,
      datasets: [{
        label: graphLabel,
        backgroundColor: 'rgb(255, 99, 132)',
        borderColor: 'rgb(255, 99, 132)',
        data: dataY,
        // backgroundColor: [
        //     'rgb(255, 99, 132)',
        //     'rgb(54, 162, 235)',
        //     'rgb(255, 205, 86)',
        //     'rgb(232,32,12)',
        //     'rgb(45,21,43)',
        //     'rgb(243,212,42)'
        // ],
      }]
    };
  
    const config = {
      type: type,
      data: data,
      options:{}
    };

    const myChart = new Chart(
      document.getElementById(elementID),
      config
    );
}


numberElementsLength = document.getElementsByClassName("number").length;
for (let i = 0; i < numberElementsLength; i++) {
    numberElement = document.getElementsByClassName("number")[i].innerHTML;
    document.getElementsByClassName("number")[i].innerHTML = numberWithCommas(numberElement);
  }
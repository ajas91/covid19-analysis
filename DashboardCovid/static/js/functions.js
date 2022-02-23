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
      }]
    };
  
    const config = {
      type: type,
      data: data,
      options:{
        elements: {
          point:{
            radius: 0
          }
        },
        title: {
          display: true,
          text: graphLabel
        }
      }
    };

    const myChart = new Chart(
      document.getElementById(elementID),
      config
    );
}


numberElementsLength = document.getElementsByClassName("numberSpan").length;
for (let i = 0; i < numberElementsLength; i++) {
    numberElement = document.getElementsByClassName("numberSpan")[i].innerHTML;
    document.getElementsByClassName("numberSpan")[i].innerHTML = numberWithCommas(numberElement);
  }
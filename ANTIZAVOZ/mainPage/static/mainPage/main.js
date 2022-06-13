$(document).ready(function () {
    labels = []
    for (var num=1; num < 15; num++){
        labels.push(num)
    }
    console.log(labels)
  
    const data = {
        labels: labels ,
        datasets: [{
        label: 'Количество замещенных категорий',
        backgroundColor: '#6c757d',
        data: 
        // canvaValues.slice(50),
        [20, 10, 5, 2, 20, 30, 45, 20, 10, 5, 2, 20, 30, 45, 9],
        }]
    };
  
  const config = {
    type: 'bar',
    data: data,
    options: {
    responsive: false,
        scales: {
            y: {
          beginAtZero: true
              }
          }
          },
      };

      const myChart = new Chart(
        document.getElementById('myChart'),
        config
      );

})
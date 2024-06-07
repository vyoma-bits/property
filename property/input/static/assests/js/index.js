const marketrentchart=document.getElementById("Maket-rent-chart");
const markertrentaskchart=document.getElementById("market-asking-rent-chart");
const askingrentchart=document.getElementById("asking-rent-chart");
const marketrentgrowthchart=document.getElementById("market-rent-growth-chart");
const mytable=document.getElementById("mytable");
new Chart(marketrentchart,{
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  new Chart(markertrentaskchart,{
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  new Chart(askingrentchart,{
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });
  new Chart(marketrentgrowthchart,{
    type: 'line',
    data: {
      labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
      datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  });

  //gpt code to maximize screen
  document.addEventListener('DOMContentLoaded', (event) => {
    const marketrentchart = document.getElementById("market-rent-chart");
    const marketaskingrentchart = document.getElementById("market-asking-rent-chart");
    const askingrentchart = document.getElementById("asking-rent-chart");
    const marketrentgrowthchart = document.getElementById("market-rent-growth-chart");

    new Chart(marketrentchart, {
        type: 'line',
        data: {
            labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
            datasets: [{
                label: '# of Votes',
                data: [12, 19, 3, 5, 2, 3],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Initialize other charts similarly...

    // Handle maximize button clicks
    const maximizeButtons = document.querySelectorAll('.maximize-btn');
    const modal = document.getElementById("chartModal");
    const modalContent = document.querySelector(".modal-content");
    const closeModal = document.querySelector(".close");
    let fullScreenChart;

    maximizeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const chartId = this.getAttribute('data-chart');
            const chartCanvas = document.getElementById(chartId);
            const chartInstance = Chart.getChart(chartId);

            if (chartInstance) {
                modal.style.display = "block";
                
                // Clone the chart data and options
                const newChartData = JSON.parse(JSON.stringify(chartInstance.data));
                const newChartOptions = JSON.parse(JSON.stringify(chartInstance.options));

                // Destroy previous fullScreenChart instance if exists
                if (fullScreenChart) {
                    fullScreenChart.destroy();
                }

                fullScreenChart = new Chart(document.getElementById('full-screen-chart'), {
                    type: chartInstance.config.type,
                    data: newChartData,
                    options: newChartOptions
                });
            }
        });
    });

    closeModal.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };
});


//adding datatable
const datatable =new simpledataTables.datatable("#mytable",{
    searchable:true,
    fixedHeight:true,
    data:{
        headings:["heading1","heading2"],
    }
})


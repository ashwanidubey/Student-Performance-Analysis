

var x = document.getElementById("info");   // Get the element with id="demo"

x.style.color = "red";
//alert(x.getAttribute('coding'))
//coding={{coding}} aptitude={{aptitude}} technical={{technical}}
//communication={{communication}} core={{core}} presentation={{presentation}}
//academics={{academics}} puzzel={{puzzel}} english={{english}}
//programming={{programming}} management={{management}}
//projects={{projects}} internship={{internship}} training={{training}} backlog={{backlog}}
var ctx = document.getElementById('myChart').getContext('2d');
var coding=x.getAttribute('coding')
var aptitude=x.getAttribute('aptitude')
var technical=x.getAttribute('technical')
var communication=x.getAttribute('communication')
var core=x.getAttribute('core')
var presentation=x.getAttribute('presentation')
var academics=x.getAttribute('academics')
var puzzel=x.getAttribute('puzzel')
var english=x.getAttribute('english')
var programming=x.getAttribute('programming')
var  management=x.getAttribute('management')
var internship=x.getAttribute('internship')
var training=x.getAttribute('training')
var backlog=x.getAttribute('backlog')
var projects=x.getAttribute('projects')
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['coding ', 'technical', 'presentation', 'puzzel solving', 'programming', 'projects','training', 'core', 'aptitude', 'communication', 'academic', 'english','management','internship','backlogs'],
        datasets: [{
            label: 'marks in different subjects',
            data: [coding, technical, presentation, puzzel,programming,projects,training,core,aptitude,communication, academics, english,management,internship,backlog],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                ,'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'

            ],
            borderWidth: 1
        }]
    },
    options: {responsive:false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        }
    }
});

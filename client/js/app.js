/*jslint browser:true */
/*global
alert, confirm, console, prompt
*/
/*global window */
var ctx = document.getElementById('myChart').getContext('2d');
console.log("kiran")
var chart = new Chart(ctx, {
  type: 'bar',
  plugins: [ChartDataSource],
  options: {
    daatasource: {
      url: 'sample-dataset.xlsx'
    }
  }
});
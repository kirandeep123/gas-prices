const createChartForEntity = (duration, filePath) => {
var parseDate = d3.timeParse("%Y-%m-%d");
  var margin = { left: 150, right: 20, top: 20, bottom: 50 };
  var width = 860 - margin.left - margin.right;
  var height = 400 - margin.top - margin.bottom;

  var max = 0;

  var xNudge = 50;
  var yNudge = 20;

  var minDate = new Date();
  var maxDate = new Date();

  d3.csv(filePath)
    .row(function(d) {
      return {
        date: parseDate(d.Date),
        price: Number(d.Price.trim().slice(1))
      };
    })
    .get(function(error, rows) {
      max = d3.max(rows, function(d) {
        return d.price;
      });
      minDate = d3.min(rows, function(d) {
        return d.date;
      });
      maxDate = d3.max(rows, function(d) {
        return d.date;
      });

      var y = d3
        .scaleLinear()
        .domain([0, max])
        .range([height, 0]);

      var x = d3
        .scaleTime()
        .domain([minDate, maxDate])
        .range([0, width]);

      var yAxis = d3.axisLeft(y);

      var xAxis = d3.axisBottom(x);

      var line = d3
        .line()
        .x(function(d) {
          return x(d.date);
        })
        .y(function(d) {
          return y(d.price);
        })
        .curve(d3.curveCardinal);

      var svg = d3
        .select("body")
        .append("svg")
        .attr("id", "svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom);
      var chartGroup = svg
        .append("g")
        .attr("class", "chartGroup")
        .attr("transform", "translate(" + xNudge + "," + yNudge + ")");

      chartGroup
        .append("path")
        .attr("class", "line")
        .attr("d", function(d) {
          return line(rows);
        });

      chartGroup
        .append("g")
        .attr("class", "axis x")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
      chartGroup
        .append("g")
        .attr("class", "axis y")
        .call(yAxis);
      chartGroup
        .append("text")
        .style("font-size", "20px")
        .style("text-decoration", "underline")
        .style("font-weight", "700")
        .attr("x", width / 2)
        .attr("y", 0 - margin.top / 322)
        .text(duration + " Prices")
        .attr("text-anchor", "right");
    });
};
var map = {
  Daily: "../data/csv/daily.csv",
  Weekly: "../data/csv/weekly.csv",
  Monthly: "../data/csv/monthly.csv",
  Annual: "https://raw.githubusercontent.com/kirandeep123/gas-prices/master/data/csv/annually.csv"
};
    for(let dur in map) {
    createChartForEntity(dur, map[dur]);
    }

const createChartForEntity = (duration, filePath) => {
  // set the dimensions and margins of the graph
  var margin = { top: 50, right: 30, bottom: 30, left: 60 },
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3
    .select("body")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  //Read the data
  d3.csv(
    filePath,
    function(d) {
      return { date: d3.timeParse("%Y-%m-%d")(d.Date), value: d.Price };
    },
    function(data) {
      // Add X axis --> it is a date format
      var x = d3
        .scaleTime()
        .domain(
          d3.extent(data, function(d) {
            return d.date;
          })
        )
        .range([0, width]);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      var y = d3
        .scaleLinear()
        .domain([
          0,
          d3.max(data, function(d) {
            return +d.value;
          })
        ])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Add the line
      svg
        .append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "black")
        .attr("stroke-width", 1.5)
        .attr(
          "d",
          d3
            .line()
            .x(function(d) {
              return x(d.date);
            })
            .y(function(d) {
              return y(d.value);
            })
        );
      svg
        .append("text")
        .style("font-size", "20px")
        .style("text-decoration", "underline")
        .style("font-weight", "700")
        .attr("text-anchor", "right")
        .attr("x", width / 2)
        .attr("y", 0 - margin.top / 122)
        .text(duration + "Prices");
    }
  );
};
var map = {
  Daily:
    "https://raw.githubusercontent.com/kirandeep123/gas-prices/master/data/csv/daily.csv",
  Weekly:
    "https://raw.githubusercontent.com/kirandeep123/gas-prices/master/data/csv/weekly.csv",
  Monthly:
    "https://raw.githubusercontent.com/kirandeep123/gas-prices/master/data/csv/monthly.csv",
  Annual:
    "https://raw.githubusercontent.com/kirandeep123/gas-prices/master/data/csv/annually.csv"
};
for(let duration in map) {
  createChartForEntity(duration, map[duration]);
}

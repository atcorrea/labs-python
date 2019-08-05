$(document).ready(function() {
    let words = getWordsInServer();

    let config = {
      width: 500,
      height: 350,
      shape: "rectangular"
    };
  
    $("#wordcloud").jQCloud(words, config);
});

// Load the Visualization API and the piechart package.
google.charts.load("current", { packages: ["corechart"] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

var chart;

function reload() {
  console.log("reloading...");
  chart.draw(getDataFromServer(), { title: "chart", width: 400, height: 240 });
}

function drawChart() {
  console.log("drawing...");

  chart = new google.visualization.PieChart(
    document.getElementById("chart_div")
  );

  var options = {
    title: "DADOS RANDOMICOS",
    width: 400,
    height: 240,
    pieHole: 0.4
  };

  chart.draw(getDataFromServer(), options);
}

function getDataFromServer() {
  let data = new google.visualization.DataTable();
  data.addColumn("string", "property");
  data.addColumn("number", "value");

  $.ajax({
    dataType: "json",
    url: "http://localhost:5000/data",
    async: false,
    success: jsonResp => {
      $.each(jsonResp, (k, v) => {
        data.addRow([k, v]);
      });
    }
  });

  return data;
}

function getWordsInServer() {
  var list = [];

  $.ajax({
    dataType: "json",
    url: "http://localhost:5000/words",
    async: false,
    success: jsonResp => {
      $.each(jsonResp, (k, v) => {
        list.push({ text: k, weight: v });
      });
    }
  });

  console.log(list);
  return list;
}

function reloadWords() {
  let words = getWordsInServer();
  $('#wordcloud').jQCloud('update', words);
}

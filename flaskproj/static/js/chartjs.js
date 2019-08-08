$(document).ready(function() {
  configWordCloud();
  drawPieChart();
});

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
  $("#wordcloud").jQCloud("update", words);
}

function configWordCloud() {
  let words = getWordsInServer();

  let config = {
    width: 500,
    height: 350,
    shape: "rectangular"
  };

  $("#wordcloud").jQCloud(words, config);
}

function drawPieChart() {
  let data = getDataFromServer("data");

  let labels = [];
  let values = [];
  $.each(data, (k, v) => {
    labels.push(k);
    values.push(v);
  });

  let cvas = document.getElementById("pie-chart").getContext("2d");
  let cfg = {
    type: "pie",
    data: {
      labels: labels,
      datasets: [
        {
          label: "pie-chart",
          data: values,
          weight: 50
        }
      ]
    }
  };

  let pieChart = new Chart(cvas, cfg);
}

function getDataFromServer(endpoint) {
  let data = {};
  let host = "http://localhost:5000/";

  $.ajax({
    dataType: "json",
    url: host + endpoint,
    async: false,
    success: jsonResp => {
      $.each(jsonResp, (k, v) => {
        data[k] = v;
      });
    }
  });

  return data;
}

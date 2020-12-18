const TrendUrl = "https://twitter-trends-daily.herokuapp.com/alltrends";
const SentimentUrl = "https://twitter-trends-daily.herokuapp.com";


fetch(TrendUrl).then(function (response) {
  return response.json();
}).then(function (TrendData) {
  console.log(TrendData);

  let TrendHTML = ``;

  for (let location in TrendData.trends) {
    if (location !== 'key') {
      var list = TrendData.trends[location];
      // console.log(list);
      TrendHTML += `
      <div class="collapsible">
    <input id="collapsible${location}" type="checkbox" name="collapsible">
    <label for="collapsible${location}">${location}</label>
    <div class="collapsible-body">
    <ul>
    `;

      for (var item in list) {
        TrendHTML +=
          `
          <li>${list[item]}</li>
          `;
      }

      TrendHTML += `</ul></div></div>`
    }
    document.getElementById("TrendsTable").innerHTML = TrendHTML;


  }

});

fetch(SentimentUrl).then(function (response) {
  return response.json();
}).then(function (SentimentData) {
  // console.log(SentimentData);

  let SentimentHTMLIndia = SentimentHTMLWorld = `<tr>
                    <th>#</th>
                    <th>Trend</th>
                    <th>Positive</th>
                    <th>Negative</th> 
                    </tr>
                    `;

  for (trend of SentimentData.trends.india) {
    SentimentHTMLIndia += `<tr>
    <td>${trend.rank}</td>
    <td><a href="https://twitter.com/search?q=${trend.name}">${trend.name}</a></td>
    <td>${trend.positive}</td>
    <td>${trend.negative}</td>
    </tr>`;
  }

  for (trend of SentimentData.trends.world) {
    SentimentHTMLWorld += `<tr>
      <td>${trend.rank}</td>
      <td><a href="https://twitter.com/search?q=${trend.name}">${trend.name}</a></td>
      <td>${trend.positive}</td>
      <td>${trend.negative}</td>
      </tr>`;
  }

  document.getElementById("contentIndia").innerHTML = SentimentHTMLIndia;
  document.getElementById("contentWorld").innerHTML = SentimentHTMLWorld;
});




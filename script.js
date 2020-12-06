const TrendUrl = "https://twitter-trends-daily.herokuapp.com/alltrends";
const SentimentUrl = "https://twitter-trends-daily.herokuapp.com";


fetch(TrendUrl).then(function (TrendData) {
  // console.log(TrendData);
});

fetch(SentimentUrl).then(function (response) {
  return response.json();
}).then(function (SentimentData) {
  console.log(SentimentData);

  let SentimentHTMLIndia = SentimentHTMLWorld = `<tr>
                    <th>#</th>
                    <th>Trend</th>
                    <th>Positive</th>
                    <th>Negative</th> 
                    </tr>
                    `;

  // let SentimentHTMLWorld = SentimentHTMLIndia;
  // console.log(SentimentData);
  for (trend of SentimentData.trends.india) {
    SentimentHTMLIndia += `<tr>
    <td>${trend.rank}</td>
    <td>${trend.name}</td>
    <td>${trend.positive}</td>
    <td>${trend.negative}</td>
    </tr>`;
  }

  for (trend of SentimentData.trends.world) {
    SentimentHTMLWorld += `<tr>
      <td>${trend.rank}</td>
      <td>${trend.name}</td>
      <td>${trend.positive}</td>
      <td>${trend.negative}</td>
      </tr>`;
  }

  document.getElementById("contentIndia").innerHTML = SentimentHTMLIndia;
  document.getElementById("contentWorld").innerHTML = SentimentHTMLWorld;



});




// let SentimentHTMLIndia = `<tr>
//                     <th>#</th>
//                     <th>Trend</th>
//                     <th>Positive</th>
//                     <th>Negative</th> 
//                     </tr>
//                     `;

// let SentimentHTMLWorld = SentimentHTMLIndia;
// console.log(SentimentData);
// for (trend in SentimentData.trends) {
//   SentimentHTMLIndia += `<tr>
//     <td>${trend.rank}</td>
//     <td>${trend.name}</td>
//     <td>${trend.positive}</td>
//     <td>${trend.negative}</td>
//     </tr>`;
// }

// document.getElementById("TrendsTable").innerHTML = SentimentHTMLIndia;


// function show(data) {
//   let tab =
//     `<tr>
//   <th>#</th>
//   <th>Trend Name</th>
//   <th>Positive</th>
//   <th>Negative</th> 
//   </tr>
//   `;
//   var count = 1;
//   for (let trend of data.trends) {
//     tab += `<tr>
//     <td>${count++}</td>
//     <td>${trend.name}</td>
//     <td>${trend.positive}</td>
//     <td>${trend.negative}</td>
//     </tr>`;
//   }

//   document.getElementById("TrendsTable").innerHTML = tab;


// }
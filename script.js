const TrendUrl = "https://twitter-trends-daily.herokuapp.com/alltrends";
const SentimentUrl = "https://twitter-trends-daily.herokuapp.com";

let deferredPrompt; // Allows to show the install prompt
const installButton = document.getElementById("install_button");

window.addEventListener("beforeinstallprompt", e => {
  console.log("beforeinstallprompt fired");
  // Prevent Chrome 76 and earlier from automatically showing a prompt
  e.preventDefault();
  // Stash the event so it can be triggered later.
  deferredPrompt = e;
  // Show the install button
  installButton.hidden = false;
  installButton.addEventListener("click", installApp);
});

function installApp() {
  // Show the prompt
  deferredPrompt.prompt();
  installButton.disabled = true;

  // Wait for the user to respond to the prompt
  deferredPrompt.userChoice.then(choiceResult => {
    if (choiceResult.outcome === "accepted") {
      console.log("PWA setup accepted");
      installButton.hidden = true;
    } else {
      console.log("PWA setup rejected");
    }
    installButton.disabled = false;
    deferredPrompt = null;
  });
}

window.addEventListener("appinstalled", evt => {
  console.log("appinstalled fired", evt);
});

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
    <ol style="display: inline-block text-align:left; list-style-position: inside;">
    `;

      for (var item in list) {
        TrendHTML +=
          `
          <li><a href="https://twitter.com/search?q=${list[item]}">${list[item]}</a></li>
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




var form = document.getElementById("inputForm");
var result_country = document.getElementById("results");

//fetch get request
fetch("https://api.covid19api.com/summary")
  .then(function (fetchRespo) {
    console.log(fetchRespo);
    return fetchRespo.json();
  })
  .then(function (fetchData) {
    console.log(fetchData);
    var iCountry;

    for (iCountry = 0; iCountry < fetchData.Countries.length; iCountry++) {
      console.log(fetchData.Countries[iCountry].Country);
    }
  })
  .catch(function (Error) {
    console.log("Error");
  });

form.addEventListener("submit", function (formSubmit) {
  formSubmit.preventDefault();
  var name = document.getElementById("name").value;
  var body = document.getElementById("body").value;
  var inputId = document.getElementById("inputId").value;
  result_country.innerHTML = "<p>this is new</p>";

  //fetch post request

  fetch("https://jsonplaceholder.typicode.com/posts", {
    method: "POST",
    body: JSON.stringify({
      title: name,
      body: body,
      id: inputId,
    }),
    headers: {
      "content-Type": "application/json; charset=UTF-8",
    },
  })
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      console.log(data);
      var result = document.getElementById("results");
      result.innerHTML = `<p> the title of the to do is ${data.title}</p>`;
    });
});

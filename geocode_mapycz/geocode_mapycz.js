function geocode(e, elm) {  /* Called during submit */
  JAK.Events.cancelDef(e); /* Prevents sending the form */
  var query = document.getElementById("query").value;
  var locality = document.getElementById("locality").value;
  var count = document.getElementById("count").value;
  var lang = document.getElementById("lang").value;
  new SMap.Geocoder(query, response, {
    locality: locality,
    count: count,
    lang: lang
  });
}

function response(geocoder) { /* Response */
  if (!geocoder.getResults()[0].results.length) {
    alert("[]");
    return;
  }

  var res = geocoder.getResults()[0].results;
  var data = []
  while (res.length) { /* Show all responses */
      var item = res.shift()
      data.push('{"coords": "' + item.coords + '", "label": "' + item.label + '"}');
  }
  alert(data.join("\n"));
}

var form = JAK.gel("form");
JAK.Events.addListener(form, "submit", geocode); /* Start geocoding when the form is submitted */

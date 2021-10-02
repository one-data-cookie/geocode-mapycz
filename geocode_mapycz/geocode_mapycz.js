function geokoduj(e, elm) {  /* Voláno při odeslání */
  JAK.Events.cancelDef(e); /* Zamezit odeslání formuláře */
  var query = document.getElementById("query").value;
  var locality = document.getElementById("locality").value;
  var count = document.getElementById("count").value;
  var lang = document.getElementById("lang").value;
  new SMap.Geocoder(query, odpoved, {
    locality: locality,
    count: count,
    lang: lang
  });
}

function odpoved(geocoder) { /* Odpověď */
  if (!geocoder.getResults()[0].results.length) {
    alert("[]");
    return;
  }

  var res = geocoder.getResults()[0].results;
  var data = []
  while (res.length) { /* Zobrazit všechny výsledky hledání */
      var item = res.shift()
      data.push('{"coords": "' + item.coords + '", "label": "' + item.label + '"}');
  }
  alert(data.join("\n"));
}

var form = JAK.gel("form");
JAK.Events.addListener(form, "submit", geokoduj); /* Při odeslání formuláře pustit geokódování */

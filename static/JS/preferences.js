function setupIndeterminate() {
  var pickInterest = document.querySelectorAll("[name=pickInterest"),
    parentInterest = document.getElementById("pickInterests");
  for (var index = 0; index < pickInterest.length; index++) {
    var cb = pickInterest[index];
    cb.addEventListener("change", function (evt) {
      var checked = 0;
      for (var j = 0; j < pickInterest.length; j++) {
        if (pickInterest[j].checked) {
          checked++;
        }
      }
      switch (checked) {
        case 0:
          parentInterest.checked = false;
          parentInterest.indeterminate = false;
          break;
        case 1:
          parentInterest.checked = false;
          parentInterest.indeterminate = true;
          break;
        default:
          parentInterest.checked = true;
          parentInterest.indeterminate = false;
          break;
      }
    });
  }
}

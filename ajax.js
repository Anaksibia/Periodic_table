function do_get() {
    var given_year = jQuery("#year").val();
    jQuery.get("disc_elements.py", {given_year: given_year}, function (array_of_elements) {
          $("h2>span").text(given_year);

          jQuery.each(array_of_elements.discovered_elements, function(index, value) {
                var elem = $("#"+value);
                if (elem.hasClass("hide")) {
                   elem.removeClass("hide");
                   elem.addClass("show");
	            }
	       })

          jQuery.each(array_of_elements.undiscovered_elements, function(index, value) {
                var elem = $("#"+value);
                if (elem.hasClass("show")) {
                   elem.removeClass("show");
                   elem.addClass("hide");
	            }
	       })
    }, "json");
}
            String.prototype.capitalize = function() {
                return this.charAt(0).toUpperCase() + this.slice(1);
            }

            $(document).submit(function(){
            var test = $("input").val();
            var city = "";
            var temp = "";
            var condition = ""
            var key1 = "http://api.openweathermap.org/data/2.5/weather?q="
            var key2 = "&appid=24f4931aaa798b5bb5ea5e03bca530c0";
                $.get("" + key1 + test + key2 + "", function(res) {
            city += "<h1>City: " + res.name + "</h1>";
            temp += "<h3>Temperature: " + Math.floor((res.main.temp * 9/5 - 459.67)) + "&deg;F" + "</h3>";
            condition += "<h3>Currently: " + res.weather[0].description.toUpperCase() + "</h3>";
            // city += res.name;
            $("#weather").html(city);
            $("#weather").append(temp);
            $("#weather").append(condition);

    
            // your code here
        }, 'json');
        // don't forget to return false so the page doesn't refresh
        return false;
    });
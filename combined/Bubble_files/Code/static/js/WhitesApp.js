d3.csv("../Resources/Whites95.csv").then (function(tableData) {
    console.log(tableData);
// })

    // from AllWines92.csv
    var tableData = tableData;

    var tbody = d3.select('tbody');

    // create function to build table

    // NEED TO DROP LAST COLUMN IN ARRAY
    function buildTable(data) {
        tbody.html("");
        data.forEach((wine) => {
            var row = tbody.append("tr");
            // Append a cell to the row for each value
            for (let [key, value] of Object.entries(wine)) {
                var cell = row.append("td");
                cell.text(value);
            }
        });
    };
    buildTable(tableData)
    // deleteColumns(tableData)
    myTable = buildTable(tableData);

    //build scatter plot
    function buildScatterPlot(data){
        var Vintage = data.map(data => data.vintage)
        var Price = data.map(data => data.price)
        var Rating = data.map(data => data.rating)
        var Title = data.map(data => data.title)
        var ID = data.map(data => data.ID)
        var Country = data.map(data => data.country)
        var Category = data.map(data => data.category)
        var Varietal = data.map(data => data.varietal)
        var URL = data.map(data => data.url)
        // var Description = data.map(data => data.description)
            
        var hoverData = [];
        var bubbleSize = [];

        for (var i=0; i < data.length; i++) {
            var hover = `<b>${Title[i]}</b><br><br><b>Varietal:</b> ${Varietal[i]}<br><b>Country:</b> ${Country[i]}<br><b>Vintage:</b> ${Vintage[i]}<br><b>Rating:</b> ${Rating[i]}<br><b>Price:</b> $${Price[i]}`
            // <br><b>Review:</b><a> href ="${URL[i]}"</a>`
            hoverData.push(hover)
            var bubSize = Price[i]
            bubbleSize.push(bubSize)
        };
        var myPlot = document.getElementById('bubble'),
            trace = {
                type: "scatter",
                x: Price,
                y: Rating,
                text: hoverData,
                mode: 'markers',
                marker: {    
                    size: bubbleSize,
                    sizemode: 'area'
                },
                transforms: [
                {
                    type: 'groupby',
                    groups: Varietal,
                }],
                hovertemplate: hoverData,
                
            },           
            data = [trace],                
            layout = {
                title: 'Price vs Rating',
                    xaxis: { title: "Price"},
                    yaxis: { title: "Rating",
                    // type: 'log'
                },
                // height: 600,
                // width: 800,
                hovermode: 'closest',
                font: {
                    family: 'sans-serif',
                    size: 10,
                  },
                position: 'left',
                xaxis: {
                    autotick: false,
                    dtick: 100,
                    title: 'Price'
                  },
                yaxis: {
                    autotick: true,
                    dtick: 1,
                    title: 'Rating'
                  }
            };
            var config = {responsive: true}
        Plotly.react("bubble", data, layout, config)
        
        myPlot.on('plotly_click', function(data){
            console.log('i clicked it!')
            console.log(data.points["0"])
            var text = data.points["0"].text
            var wineInfo = document.getElementById('wine-description').innerHTML=text;
          })
    };
    buildScatterPlot(tableData);

    // create lists for dropdowns
    CategoryList = ["", "Red", "White", "Sparkling", "Rose", "Dessert", "Port/Sherry", "Fortified"]
    VinList = ["",2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
    PriceList = ["","0-25","26-50","51-100","101+"]
    VarietalList = [""]
    RatingList = [""]
    CountryList = [""]

    // create list for ratings from data
    for (var i=0; i<tableData.length; i++) {
        ratings = tableData[i].rating
        RatingList.push(ratings)
    };

    // remove duplicates from RatingList and sort
    var RatingList2 = Array.from(new Set(RatingList)).sort()
    // console.log(RatingList2);

    // populate CountryList from countries in dataset
    for (var i=0; i<tableData.length; i++) {
        countries = tableData[i].country
        CountryList.push(countries)
    };
    // remove duplicates from CountryList and sort
    var CountryList2 = Array.from(new Set(CountryList)).sort()
    // console.log(CountryList2);

    // populate VarietalList from countries in dataset
    for (var i=0; i<tableData.length; i++) {
        varietals = tableData[i].varietal
        VarietalList.push(varietals)
    };
    // remove duplicates from CountryList and sort
    var VarietalList2 = Array.from(new Set(VarietalList)).sort()
    console.log(VarietalList2);

    // lists = [VinList, PriceList, RatingList, CountryList2];
    // ids = [selVintage, selPrice, selRating, selCountry]

    // assign lists to dropdowns
    var sel = document.getElementById('selVarietal');
    var fragment = document.createDocumentFragment();

    VarietalList2.forEach(function(category, index) {
        var opt = document.createElement('option');
        opt.innerHTML = category;
        opt.value = category;
        fragment.appendChild(opt);
    });
    sel.appendChild(fragment);
    // console.log(sel)
    
    var sel = document.getElementById('selVintage');
    var fragment = document.createDocumentFragment();

    VinList.forEach(function(vintage, index) {
        var opt = document.createElement('option');
        opt.innerHTML = vintage;
        opt.value = vintage;
        fragment.appendChild(opt);
    });
    sel.appendChild(fragment);
    console.log(sel)

    var sel = document.getElementById('selPrice');
    var fragment = document.createDocumentFragment();

    PriceList.forEach(function(price, index) {
        var opt = document.createElement('option');
        opt.innerHTML = price;
        opt.value = price;
        fragment.appendChild(opt);
    });
    sel.appendChild(fragment);

    var sel = document.getElementById('selRating');
    var fragment = document.createDocumentFragment();

    RatingList2.forEach(function(rating, index) {
        var opt = document.createElement('option');
        opt.innerHTML = rating;
        opt.value = rating;
        fragment.appendChild(opt);
    });
    sel.appendChild(fragment);

    var sel = document.getElementById('selCountry');
    var fragment = document.createDocumentFragment();

    CountryList2.forEach(function(country, index) {
        var opt = document.createElement('option');
        opt.innerHTML = country;
        opt.value = country;
        fragment.appendChild(opt);
    });
    sel.appendChild(fragment);
    
    // create variable for button id
    var button = d3.select("#filter-btn");

    button.on("click", () => {
        
        // get value of input in form
        var inputVarietal = d3.select("#selVarietal").property("value");
        var inputVintage = d3.select("#selVintage").property("value");
        var inputRating = d3.select("#selRating").property("value");
        var inputPrice = d3.select("#selPrice").property("value");
        var inputCountry = d3.select("#selCountry").property("value");
        
        // function priceChoice(inputPrice,filteredPrice) {
        if (inputPrice === PriceList[0]) {
            filteredPrice = tableData.filter(data => data.price);
            } else if (inputPrice === PriceList[1]) {
            filteredPrice = tableData.filter(data => data.price<26);
            } else if (inputPrice === PriceList[2]) {
            filteredPrice = tableData.filter(data => data.price<51 && data.price>25);
            } else if (inputPrice === PriceList[3]) {
            filteredPrice = tableData.filter(data => data.price<101 && data.price>50);
            } else {
            filteredPrice = tableData.filter(data => data.price>100);
            }

        // filter dataset by input from above
        var filteredVarietal = tableData.filter(data => data.varietal === inputVarietal);
        var filteredVintage = tableData.filter(data => data.vintage === inputVintage);
        var filteredRating= tableData.filter(data => data.rating === inputRating)
        var filteredCountry = tableData.filter(data => data.country === inputCountry);

        function getCommon(arr1, arr2) {
            var common = [];
            if(arr2.length>0) {
                for(var i=0 ; i<arr1.length ; ++i) {
                    for(var j=0 ; j<arr2.length ; ++j) {    
                        if(arr1[i] == arr2[j]) {
                            common.push(arr1[i]);
                        }
                    }
                }
            return common;                     // Return the common elements
            }
            else {
                return arr1
            }
        };
        var filteredArray0 = getCommon(tableData, filteredVarietal);
        var filteredArray1 = getCommon(filteredArray0, filteredVintage);
        var filteredArray2 = getCommon(filteredArray1,filteredRating);
        var filteredArray3 = getCommon(filteredArray2, filteredPrice);
        var filteredArray4 = getCommon(filteredArray3, filteredCountry);
       
        // check if combinedArray is empty and if so return original tableData data
        // if not empty fill table with filtered results
        if (!Array.isArray(filteredArray4) || !filteredArray4.length) 
            buildTable(tableData);
            else 
                buildTable(filteredArray4), 
                buildScatterPlot(filteredArray4)
    });
});
// d3.csv("../Resources/CategoryData.csv").then (function(tableData) {
//     console.log(tableData);
// })




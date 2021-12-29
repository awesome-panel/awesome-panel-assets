// Tested with panel 0.12.6, Tabulator 5.0.7, jquery-1.12.4.min.js and 2.1.2/jquery.sparkline.min.js
//Formatter to generate line chart
var lineFormatter = function(cell, formatterParams, onRendered){
    onRendered(function(){ //instantiate sparkline after the cell element has been aded to the DOM
        $(cell.getElement()).sparkline(cell.getValue(), {width:"100%", type:"line", disableTooltips:true});
    });
};

//generate bar chart
var barFormatter = function(cell, formatterParams, onRendered){
    onRendered(function(){ //instantiate sparkline after the cell element has been aded to the DOM
        $(cell.getElement()).sparkline(cell.getValue(), {width:"100%", type:"bar", barWidth:14, disableTooltips:true});
    });
};

//generate discrete chart
var tristateFormatter = function(cell, formatterParams, onRendered){
    onRendered(function(){ //instantiate sparkline after the cell element has been aded to the DOM
        $(cell.getElement()).sparkline(cell.getValue(), {width:"100%", type:"tristate", barWidth:14, disableTooltips:true});
    });
};


//generate box plot
var boxFormatter = function(cell, formatterParams, onRendered){
    onRendered(function(){ //instantiate sparkline after the cell element has been aded to the DOM
        $(cell.getElement()).sparkline(cell.getValue(), {width:"100%", type:"box", disableTooltips:true});
    });
};

Tabulator.moduleBindings["format"].formatters['spark_line'] = lineFormatter
Tabulator.moduleBindings["format"].formatters['spark_bar'] = barFormatter
Tabulator.moduleBindings["format"].formatters['spark_tristate'] = tristateFormatter
Tabulator.moduleBindings["format"].formatters['spark_box'] = boxFormatter
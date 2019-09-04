$(document).ready(function(){
    $("#search-text").keyup(function(){
    _this = this;

    $.each($("#info-tableCustomers tbody tr"), function() {
        if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) {
            $(this).hide();
        } else {
            $(this).show();                
        }
    });

    $.each($("#info-tableCars tbody tr"), function() {
        if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) {
            $(this).hide();
        } else {
            $(this).show();                
        }
      });

      $.each($("#info-tableOrders tbody tr"), function() {
        if($(this).text().toLowerCase().indexOf($(_this).val().toLowerCase()) === -1) {
            $(this).hide();
        } else {
            $(this).show();                
        }
      });
    });
});
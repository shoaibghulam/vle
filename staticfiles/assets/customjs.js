
$(document).ready(function(){
  $('#add-morebtninv').hide();
    $("#bankselect").change(function(){
       if($('#bankselect').val() == 'checking')
       {
       		$('.checkdiv').css('display','block');
       		$('.savingdiv').css('display','none');
       	    $('.cssdiv').css('display','none');
       }
       if($('#bankselect').val() == 'css')
       {
       	    $('.cssdiv').css('display','block');
       	    $('.checkdiv').css('display','none');
       	    $('.savingdiv').css('display','none');
       	   
       }
       if($('#bankselect').val() == 'saving')
       {
       		$('.savingdiv').css('display','block');
       	    $('.checkdiv').css('display','none');
       	    $('.cssdiv').css('display','none');
       	   
       }
       if($('#bankselect').val() == 'default')
       {
       		$('.savingdiv').css('display','none');
       	    $('.checkdiv').css('display','none');
       	    $('.cssdiv').css('display','none');
       	   
       }
       if($('#bankselect').val() == 'default')
       {
                  $('.mutualfund').css('display','none');
                $('.annuityvar').css('display','none');
                $('.annuityfix').css('display','none');
                $('.annuityindex').css('display','none');
               
       }
       if($('#bankselect').val() == 'mutualfunds')
       {
                  $('.mutualfund').css('display','block');
                $('.annuityvar').css('display','none');
                $('.annuityfix').css('display','none');
                $('.annuityindex').css('display','none');
               
       }
       if($('#bankselect').val() == 'annuityvar')
       {
                  $('.annuityvar').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityfix').css('display','none');
                  $('.annuityindex').css('display','none');
               
       }
        if($('#bankselect').val() == 'annuityfix')
       {
                  $('.annuityfix').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityvar').css('display','none');
                  $('.annuityindex').css('display','none');
               
       }
       if($('#bankselect').val() == 'annuityindex')
       {
                  $('.annuityindex').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityvar').css('display','none');
                  $('.annuityfix').css('display','none');
       }


    });
    $('#investmentselect').change(function(){
       if($('#investmentselect').val() == 'default')
       {
                  $('.mutualfund').css('display','none');
                $('.annuityvar').css('display','none');
                $('.annuityfix').css('display','none');
                $('.annuityindex').css('display','none');
               
       }
       if($('#investmentselect').val() == 'mutualfunds')
       {
            alert("mutualfund Selected");
                  $('.mutualfund').css('display','block');
                $('.annuityvar').css('display','none');
                $('.annuityfix').css('display','none');
                $('.annuityindex').css('display','none');
               
       }
       if($('#investmentselect').val() == 'annuityvar')
       {
                  $('.annuityvar').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityfix').css('display','none');
                  $('.annuityindex').css('display','none');
               
       }
        if($('#investmentselect').val() == 'annuityfix')
       {
                  $('.annuityfix').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityvar').css('display','none');
                  $('.annuityindex').css('display','none');
               
       }
       if($('#investmentselect').val() == 'annuityindex')
       {
                  $('.annuityindex').css('display','block');
                  $('.mutualfund').css('display','none');
                  $('.annuityvar').css('display','none');
                  $('.annuityfix').css('display','none');
       }


    });

//function for show and hide button  on switch tabs 
    $('#inv').click(function(){
      $('#add-morebtn').hide();
      $('#add-morebtninv').show();

    });
    $('#bank').click(function(){
      $('#add-morebtn').show();
      $('#add-morebtninv').hide();
    });



      //function for Cloning Form Bank Div
    $('#add-morebtn').click(function(){
      
      $('#clonedItem').css('display','block');
      var $orginal = $('#bankform');
      var $cloned = $orginal.clone();

      //get original selects into a jq object
      var $originalSelects = $orginal.find('#bankselect');
      $cloned.find('#bankselect').each(function(index, item) {
     //set new select to value of old select
     $(item).val( $originalSelects.eq(index).val() );

 
      });
            
      $cloned.appendTo('#clonedItem');
      $('#removediv').show();
      
      });



// $('#removediv').hide();
});

//function for Removing Form Bank Div

$('#removediv').click(function(){
      $('#clonedItem').css('display','none');
      // $('#removediv').hide();
});

//Data Table Initialize 

$('#kt_table').DataTable();



















// var clone = $('#kt_portlet_base_demo_1_1_tab_content').clone('#bankform');

      // $('#kt_portlet_base_demo_1_1_tab_content').append(clone);
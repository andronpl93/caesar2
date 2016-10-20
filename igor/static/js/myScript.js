jQuery(function($){
var errors;

    initDiagram();
    
    $('button').bind('click',function(event){
        $(this).addClass('fakeActive');
        $(this).removeClass('Hover');
        var obj={
                type:'POST',
                dataType:'json', 
                data: {
                    'lef'   : $('textarea[name=lef]').val(),
                    'inText': $('[name=inText]').val()
                    },
                error:function(){
                    elem=$('.myError')
                    elem.append('<p>Произошла какая-то ошибка. </br>Ну хз, попробуйте еще раз</p>');
                    elem.animate({'opacity':'1'},400);
                    activeOff();
                    },
                success: function(data){
                    activeOff();
                    $('#vang > span').remove();
                        if(data.errors.length){
                            
                            errors=data.errors;
                            elem=$('.myError')
                            elem.append('<p>'+errors.pop()+'</p>');
                            elem.animate({'opacity':'1'},400);
                            
                        }
                        else{
                            if (event.target.name!='vanga'){
                                $('textarea[name=rig]').val(data.result.join(""));
                            }
                            diagramResult(data);
                            if (data.massage)
                            {
                                $('#vang').append('<span>'+data.massage+'</span>');
                            }
                                
                        }

                }
        }
        
        
        if (event.target.name=='decoder' || event.target.name=='encoder' || event.target.name=='vanga'){
            obj.url='/'+event.target.name+'/'; 
            $.ajax(obj);            
        }
        if( event.target.name=='kidok' )
        {   
            if($('textarea[name=rig]').val().length>0)
            {
                $('textarea[name=lef]').val($('textarea[name=rig]').val());
                $('textarea[name=rig]').val(''); 
            }
            activeOff();
        }

    });
    
    
    
    $('.myError').bind('click',function(event){

       if (event.target.tagName=='SPAN'){
           $(this).animate({'opacity':'0'},400,function(){
              $('p',this).remove();
                if(errors.length>0)
                {
                    $(this).append('<p>'+errors.pop()+'</p>').animate({'opacity':'1'},200);;
                }
           });
           
       }
        
    });
    

});   


function activeOff(){
    elem=$('button.fakeActive');
    elem.addClass('Hover');
    elem.removeClass('fakeActive');
    
}

function diagramResult(obj){
    $('.tower').each(function(i,elem){
         elem.style.height=obj.norm[i]+'%';  
         $('span:first',elem).empty().append(obj.chastota[i]);  
    });
}      
 

function initDiagram(){
    for (var i=0;i<26;i++){
        $('#diagram').append('<div class="tower" style="height:1%"><p><span >0</span></br><span class="chastota">'+String.fromCharCode(97+i)+'</span></p></div>');
    }
}



/*csrf_token */   
     
 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

     
                    

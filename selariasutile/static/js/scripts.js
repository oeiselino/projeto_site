/*
    Slider
*/
$(window).load(function() {
    $('.flexslider').flexslider({
        animation: "slide",
    });
});


/*
    Filterable galeria
*/
jQuery(document).ready(function() {
    $clientsHolder = $('ul.galeria-img');
    $clientsClone = $clientsHolder.clone(); 
 
    $('.filtro-galeria a').click(function(e) {
        e.preventDefault();
        $filtroClass = $(this).attr('class');
 
        $('.filtro-galeria a').attr('id', '');
        $(this).attr('id', 'active-imgs');
 
        if($filterClass == 'all'){
            $filters = $clientsClone.find('li');
        }
        else {
            $filters = $clientsClone.find('li[data-type~='+ $filterClass +']');
        }
 
        $clientsHolder.quicksand($filters, {duration: 700}, function() {
            $("a[rel^='prettyPhoto']").prettyPhoto({social_tools: false});
        });
    });
});


/*
    Pretty Photo
*/
jQuery(document).ready(function() {
    $("a[rel^='prettyPhoto']").prettyPhoto({social_tools: false});
});


/*
    Google maps
*/
jQuery(document).ready(function() {
    var position = new google.maps.LatLng(45.067883, 7.687231);
    $('.map').gmap({'center': position,'zoom': 15, 'disableDefaultUI':true, 'callback': function() {
            var self = this;
            self.addMarker({'position': this.get('map').getCenter() });	
        }
    });
});


/*
    Contact form
*/
jQuery(document).ready(function() {
    $('.contato-caixa formulario').submit(function() {

        $('.contato-caixa formulario .nameLabel').html('Name');
        $('.contato-caixa formulario .emailLabel').html('Email');
        $('.contato-caixa formulario .messageLabel').html('Message');

        var postdata = $('.contato-caixa formulario').serialize();
        $.ajax({
            type: 'POST',
            url: 'assets/sendmail.php',
            data: postdata,
            dataType: 'json',
            success: function(json) {
                if(json.nameMessage != '') {
                    $('.contato-caixa formulario .nameLabel').append(' - <span class="cor" style="font-size: 13px; font-style: italic"> ' + json.nameMessage + '</span>');
                }
                if(json.emailMessage != '') {
                    $('.contato-caixa formulario .emailLabel').append(' - <span class="cor" style="font-size: 13px; font-style: italic"> ' + json.emailMessage + '</span>');
                }
                if(json.messageMessage != '') {
                    $('.contato-caixa formulario .messageLabel').append(' - <span class="cor" style="font-size: 13px; font-style: italic"> ' + json.messageMessage + '</span>');
                }
                if(json.nameMessage == '' && json.emailMessage == '' && json.messageMessage == '') {
                    $('.contato-caixa formulario').fadeOut('fast', function() {
                        $('.contato-caixa').append('<p><span class="cor">Thanks for contacting us!</span> We will get back to you very soon.</p>');
                    });
                }
            }
        });
        return false;
    });
});


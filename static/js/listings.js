$(document).ready(function() {
   $('#search-btn').on( 'click', function(e) {
       e.preventDefault();
       var searchText = $('#search-box').val();
       $.ajax( {
           url: '/my_listings?search_filter=' + searchText,
           type: 'GET',
           success: function(resp) {
               var newHtml = resp.data.map(d => {
                   return ´<div class="Single_listing">
                                <a href="/my_listings/${d.id}">
                                    <img class="listing_img" src="${d.listing_image_url" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>´
               });
               $('.list-listings').html(newHtml.join(''));
               $('#search-box').val('');
           },
           error: function(xhr, status, error) {
                console.error(error);
           }
       })
   });
});
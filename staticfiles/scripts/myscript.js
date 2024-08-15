$(document).ready(function(){
    let sidebar = $(".sidebar");
    let sidebar_close = $(".sidebar_close");
    let sidebar_container = $(".sidebar_container");

    sidebar.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "block");
        sidebar.css("display", "none");
        sidebar_container.css("display","flex");
        sidebar_close.css("display", "block");
    });

    sidebar_close.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "none");
        sidebar_close.css("display", "none");
        sidebar_container.css("display","none");
        sidebar.css("display", "block");
    });
    document.querySelector('.profile-icon').addEventListener('mouseenter', function() {
        document.querySelector('.dropdown-content').style.display = 'block';
      });
      
      document.querySelector('.profile-dropdown').addEventListener('mouseleave', function() {
        document.querySelector('.dropdown-content').style.display = 'none';
      });
});

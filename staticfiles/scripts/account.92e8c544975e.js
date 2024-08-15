$(document).ready(function(){
    let sidebar = $(".sidebar");
    let sidebar_close = $(".sidebar_close");
    let sidebar_container = $(".sidebar_container");
    let account = $("#account_button");
    let settings = $("#settings_button");
    let friends = $("#friends")
    sidebar.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "block");
        sidebar.css("display", "none");
        sidebar_container.css("display","flex");
        sidebar_close.css("display", "block");
    });

    friends.on("click", function(){
        
        $(".account3").css("display","block")
        $(".account2").css("display","none")
        $(".account").css("display","none")
        friends.css("color","rgb(255, 117, 31)")
        account.css("color","white")
        settings.css("color","white")
        

    })

    sidebar_close.on("click", function(e){
        e.preventDefault();
        $(".dropdown_menu").css("display", "none");
        sidebar_close.css("display", "none");
        sidebar_container.css("display","none");
        sidebar.css("display", "block");
    });

    account.on("click",function(e){
        e.preventDefault();
        $(".account").css("display","block")
        $(".account2").css("display","none")
        account.css("color","rgb(255, 117, 31)")
        settings.css("color","white")
        friends.css("color","white")

    })

    settings.on("click",function(e){
        e.preventDefault();
        $(".account").css("display","none")
        $(".account2").css("display","block")
        settings.css("color","rgb(255, 117, 31)")
        account.css("color","white")
        friends.css("color","white")




    })

});

class Main_page_1_menu_login
{
    constructor(root) {
        this.root = root;
        this.$login = $(
            `
           <a style = "color:white;"><a href = "login/" style = "position:absolute; right:5%;" class = "a1"> <b>Sign in </b></a></a>
            `
        );
        this.$logout = $(
            `
            <div class = "dropdown">
            <a style = "color:white;" class = "dropbtn"><a style = "position:absolute; right:4%;" class = "a1 logined_title">sdd <b></b></a></a>
            <br>
            <br>
            <div class = "dropdown_content">
            <a href = "login/logout/"> Sign out </a>
            <a href = "/userinfo/" class = "user_settings">Settings</a>
            </div>
            </div>
            `
        );
        this.$login.hide();
        this.$logout.hide();
        this.$username = this.$logout.find(".logined_title");
        this.$usersettings = this.$logout.find('.user_settings');
        this.root.$main_page_1_menu.append(this.$login);
        this.root.$main_page_1_menu.append(this.$logout);
        this.start();
    }   
    start() {
        this.get_info();
    }
    logout() {
        let outer = this;
        $.ajax({
            url : "login/logout/",
            type: "GET",
            success:function(resp) {
                if (resp.result == "success") {
                    location.reload();
                }
            }
        })
    }
    logined() {
        this.$login.hide();
        this.$logout.show();
    } 
    unlogin() {
        this.$login.show();
        this.$logout.hide();
    }
    get_info() {
        let outer = this;
        $.ajax ({
            url: "/login/getinfo/",
            type:"GET" ,
            success:function(resp) {
                if (resp.result === "success") {
                    console.log("openname: " + outer.$username.val());
                    outer.logined();
                    document.getElementsByClassName("logined_title")[0].innerHTML = "<b>" + resp.open_name + "</b>";
                    document.getElementsByClassName("user_settings")[0].href = "user_info/" + resp.uid;
                    console.log("opennamew: " +  document.getElementsByClassName("user_settings")[0].href);
                } else {
                    outer.unlogin();
                }
            }
            
        });
    }
}

export class Main_page_1_menu 
{
    constructor(id) {
        this.$main_page_1_menu = $('#' + id);
        this.login = new Main_page_1_menu_login(this);
    }
}
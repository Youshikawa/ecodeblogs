class Main_page_1_menu_login
{
    constructor(root) {
        this.root = root;
        this.$login = $(
            `
            <a href = "login/">
                <botton class = "main_page_1_menu_login"> login </botton>
            </a>
            `
        );
        this.$logout = $(
            `
            <a href = "login/logout/">
                <botton id = "main_page_1_menu_logout" class = "main_page_1_menu_login"> logout </botton>
            </a>
            `
        );
        this.$login.hide();
        this.$logout.hide();
        this.root.$main_page_1_menu.append(this.$login);
        this.root.$main_page_1_menu.append(this.$logout);
        this.start();
    }   
    start() {
        this.get_info();
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
                    outer.logined();
                } else {
                    outer.unlogin();
                }
                console.log(res);
            }
            
        });
        return res;
    }
}

export class Main_page_1_menu 
{
    constructor(id) {
        this.$main_page_1_menu = $('#' + id);
        this.login = new Main_page_1_menu_login(this);
    }
}
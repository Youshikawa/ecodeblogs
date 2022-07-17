class Login_page_pane {
    constructor(root) {
        this.root = root;
        this.$login = $(`
            <div>
                <h1 class = "login_page_pane_title"> Sign in </h1>
                <br>
                <input class = "login_page_input login_page_pane_username"placeholder="Please enter username"> <br>
                <br>
                <input class = "login_page_input login_page_pane_password" class = "password" type="password" placeholder="Please enter password"> <br>
                <br>
                <button class = "login_page_button login_page_login_button" > login </button> <br>
                <br>
                <br>
                <h5> Don't have an account yet? </h5>
                <button  class = "to_register"> register now! </button >
            </div>
        `);
        this.$register = $(`
            <div>
                <h1 class = "login_page_pane_title"> Register </h1>
                <br>
                <input class = "login_page_input register_page_pane_username" placeholder="Please enter username"> <br>
                <br>
                <input class = "login_page_input register_page_pane_password" class = "password" type="password" placeholder="Please enter password"> <br>
                <br><input class = "login_page_input register_page_pane_password_confirm"  class = "password" type="password" placeholder="Confirm password"> <br>
                <br>
                <button class = "login_page_button register_page_login_button" > register </button> <br>
            </div>
        `);
        this.$login_error_msg = $(`<div>   <h1 style = "color:red; font-size:350%;">!</h1><h1 style = "color:red" class = "login_page_pane_title"> Attention </h1>  </div> <h4> Wrong username or password </h4> <br><br><br><a href = "/login"> <button class = "login_page_button"> Retry </button> </a> </div>`) 
        this.$register_error_msg_null = $(`<div>   <h1 style = "color:red; font-size:350%;">!</h1><h1 style = "color:red" class = "login_page_pane_title"> Attention </h1>  </div> <h4> Username and password can't be null </h4> <br><br><br><a href = "/login"> <button class = "login_page_button"> Retry </button> </a> </div>`) 
        this.$register_error_msg_exists = $(`<div>   <h1 style = "color:red; font-size:350%;">!</h1><h1 style = "color:red" class = "login_page_pane_title"> Attention </h1>  </div> <h4> Username is already existed </h4> <br><br><br><a href = "/login"> <button class = "login_page_button"> Retry </button> </a> </div>`) 
        this.$register_error_msg_confirm = $(`<div>   <h1 style = "color:red; font-size:350%;">!</h1><h1 style = "color:red" class = "login_page_pane_title"> Attention </h1>  </div> <h4> Password confirm faild </h4> <br><br><br><a href = "/login"> <button class = "login_page_button"> Retry </button> </a> </div>`) 
        this.$register_error_msg_allow = $(`<div>   <h1 style = "color:red; font-size:350%;">!</h1><h1 style = "color:red" class = "login_page_pane_title"> Attention </h1>  </div> <h4> Password must consist with more than 8 letters and numbers </h4> <br><br><br><a href = "/login"> <button class = "login_page_button"> Retry </button> </a> </div>`) 
        this.$register_success = $(`<div>   <h1 style = "color:green; font-size:350%;"> ^w^ つ </h1><h1 style = "color:green" class = "login_page_pane_title"> Congratulate </h1>  </div> <h4> Welcome to use ecodeblogs </h4> <br><br><br><a href = "/"> <button class = "login_page_button"> Start! </button> </a> </div>`) 
        this.root.$Login_page.append(this.$register_error_msg_allow );
        this.root.$Login_page.append(this.$register_success);
        this.root.$Login_page.append(this.$login);
        this.root.$Login_page.append(this.$register_error_msg_confirm);
        this.root.$Login_page.append(this.$login_error_msg);
        this.root.$Login_page.append(this.$register_error_msg_null);
        this.root.$Login_page.append(this.$register_error_msg_exists);
        this.$register_success.hide();
        this.$register_error_msg_allow.hide();
        this.$register_error_msg_exists.hide();
        this.$register_error_msg_confirm.hide();
        this.$register_error_msg_null.hide();
        this.$login_error_msg.hide();
        this.root.$Login_page.append(this.$register);
        this.$register.hide();
        this.$to_register = this.$login.find(".to_register");
        this.$login_username = this.$login.find(".login_page_pane_username");
        this.$login_password = this.$login.find(".login_page_pane_password");
        this.$login_submit = this.$login.find(".login_page_button");

        this.$register_username = this.$register.find(".register_page_pane_username");
        this.$register_password = this.$register.find(".register_page_pane_password");
        this.$register_password_confirm = this.$register.find(".register_page_pane_password_confirm");
        this.$register_submit = this.$register.find(".register_page_login_button");
        this.$login.show();
        this.start();
    }
    start() {
        this.status = "login";
        let outer = this;
        $(window).keydown(function(e){
            if(e.which === 13 && this.status === "login"){
                outer.login();
            } else if (e.which === 13) {
                outer.register();
            }
        })
        this.$to_register.click(function(){ 
            this.status = "register";
            outer.$login.hide();
            outer.$register.show();
        })
        this.getinfo();
        this.$login_submit.click(function(){
            outer.login();
        });
        this.$register_submit.click(function(){
            outer.register();
        });
    }
    
    register() {
        let outer = this;
        let username = this.$register_username.val();
        let password = this.$register_password.val();
        let password_confirm = this.$register_password_confirm.val();

        $.ajax({
            url: "/login/register",
            type: "GET",
            data : {
                username:username,
                password:password,
                password_confirm : password_confirm,
            },
            success:function(resp) {
                console.log(resp);
                if (resp.result === "success") {
                    outer.$register_success.show();
                    outer.$register.hide();
                } else if (resp.result === "info_null" ) {
                    outer.$register.hide();
                    outer.$register_error_msg_null.show();
                } else if (resp.result === "username_exist") {
                    outer.$register_error_msg_exists.show();
                    outer.$register.hide();
                } else if (resp.result === "password_not_allowed") {
                    outer.$register_error_msg_allow.show();
                    outer.$register.hide();
                } else if (resp.result === "password_confirm_error") {
                    outer.$register_error_msg_confirm.show();
                    outer.$register.hide();
                }
            } 
        })

    }

    login() {
        let outer = this;
        let password = this.$login_password.val();
        let username = this.$login_username.val();
        $.ajax ({
            url: "/login/signin/",
            type:"GET" ,
            data : {
                username:username ,
                password:password ,
            } ,
            success:function(resp) {
                console.log(resp);
                if (resp.result === "success") {
                    window.location.replace('/');
                } else {
                    outer.$login.hide();
                    outer.$login_error_msg.show();
                } 
            }
            
        });
    }
    //  如果登录了， 那么就直接跳转到主业
    getinfo() {
        let outer = this;
        $.ajax ({
            url: "/login/getinfo/",
            type:"GET" ,
            success:function(resp) {
                console.log(resp);
                if (resp.result === "success") {
                    window.location.replace('/');
                } 
            }
            
        });
    }
}
export class Login_page {
    constructor(id) {
        this.$Login_page = $('#' + id);
        this.$Login_page_pane = new Login_page_pane(this);
    }
}
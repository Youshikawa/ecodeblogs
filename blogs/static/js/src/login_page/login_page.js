class Login_page_pane {
    constructor(root) {
        this.root = root;
        this.$login = $(`
            <div>
                <h1 class = "login_page_pane_title"> Sign in </h1>
                <br>
                <input class = "login_page_input" class = "login_page_pane_username" placeholder="Please enter username"> <br>
                <br>
                <input class = "login_page_input" class = "login_page_pane_password" class = "password" type="password" placeholder="Please enter password"> <br>
                <br>
                <button class = "login_page_button" class = "login_page_login_button"> login </button> <br>
                <br>
                <br>
                <h5> No account ? </h5>
                <button  class = "to_register"> register now! </button >
            </div>
        `);
        this.$register = $(`
            <div>
                <h1 class = "login_page_pane_title"> Register </h1>
                <br>
                <input class = "login_page_input" class = "register_page_pane_username" placeholder="Please enter username"> <br>
                <br>
                <input class = "login_page_input" class = "register_page_pane_password" class = "password" type="password" placeholder="Please enter password"> <br>
                <br><input class = "login_page_input" class = "register_page_pane_password_confirm" class = "password" type="password" placeholder="Confirm password"> <br>
                <br>
                <button class = "login_page_button" class = "register_page_login_button"> register </button> <br>
            </div>
        `);
        this.root.$Login_page.append(this.$login);
        this.root.$Login_page.append(this.$register);
        this.$register.hide();
        this.$to_register = this.$login.find(".to_register");
        this.$login.show();
        this.start();
    }
    start() {
        let outer = this;
        this.$to_register.click(function(){
            outer.$login.hide();
            outer.$register.show();
        })
    }
}
export class Login_page {
    constructor(id) {
        this.$Login_page = $('#' + id);
        this.$Login_page_pane = new Login_page_pane(this);
    }
}
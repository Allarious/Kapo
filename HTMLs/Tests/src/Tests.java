import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.io.File;

public class Tests {

    public static void main(String[] args) throws InterruptedException {

        File gecko = new File("/Users/a11/Desktop/HTMLs/geckodriver");
        System.setProperty("webdriver.gecko.driver", gecko.getAbsolutePath());

        WebDriver driver = new FirefoxDriver();
        driver.get("file:///Users/a11/Desktop/HTMLs/ContactUs/index.html");

        WebElement text = driver.findElement(By.id("contact-text"));
        WebElement userName = driver.findElement(By.id("username"));
        WebElement email = driver.findElement(By.id("email"));
        WebElement phone = driver.findElement(By.id("phone"));
        WebElement webSite = driver.findElement(By.id("website"));
        WebElement message = driver.findElement(By.id("message"));
        WebElement submitButton = driver.findElement(By.id("contact-submit"));

        ////Thread.sleep(2000);
        submitButton.click();
        if (text.getText().equals("Please Fill Name Field"))
        {
            System.out.println("Test 1 Passed contact_us");
        } else {
            System.out.println("Test 1 Failed contact_us");
        }

        //Thread.sleep(2000);
        userName.sendKeys("Allarious");
        submitButton.click();
        //Thread.sleep(2000);
        if (text.getText().equals("Please Fill Email Field"))
        {
            System.out.println("Test 2 Passed contact_us");
        } else {
            System.out.println("Test 2 Failed contact_us");
        }

        //Thread.sleep(2000);
        email.sendKeys("NotInEmailFormat");
        submitButton.click();
        //Thread.sleep(2000);
        if (text.getText().equals("Please Enter Email Correctly"))
        {
            System.out.println("Test 3 Passed contact_us");
        } else {
            System.out.println("Test 3 Failed contact_us");
        }

        //Thread.sleep(2000);
        email.clear();
        email.sendKeys("Allarious@kapo.com");
        submitButton.click();
        //Thread.sleep(2000);
        if (text.getText().equals("Please Enter Text"))
        {
            System.out.println("Test 4 Passed contact_us");
        } else {
            System.out.println("Test 4 Failed contact_us");
        }

        //Thread.sleep(2000);
        message.sendKeys("I wish you a really good day :)");
        submitButton.click();
        //Thread.sleep(2000);
        if (text.getText().equals("Contact Form"))
        {
            System.out.println("Test 5 Passed contact_us");
        } else {
            System.out.println("Test 5 Failed contact_us");
        }

        //Thread.sleep(5000);

        //**************************************



        driver.get("file:///Users/a11/Desktop/HTMLs/LoginPage/index.html");
        text = driver.findElement(By.id("welcome"));
        userName = driver.findElement(By.id("login_username"));
        WebElement passWord = driver.findElement(By.id("login_password"));
        WebElement loginButton = driver.findElement(By.id("login_button"));
        WebElement forgetPassWord = driver.findElement(By.id("forget-label"));

        //Thread.sleep(2000);
        userName.sendKeys("Allarious");
        //Thread.sleep(2000);
        passWord.sendKeys("12345");
        //Thread.sleep(2000);
        loginButton.click();
        if (text.getText().equals("Access Granted"))
        {
            System.out.println("Test 1 Passed login");
        } else {
            System.out.println("Test 1 Failed login");
        }

        //Thread.sleep(2000);
        userName.clear();
        userName.sendKeys("NotAUser");
        //Thread.sleep(2000);
        passWord.clear();
        passWord.sendKeys("12333");
        //Thread.sleep(2000);
        loginButton.click();
        if (text.getText().equals("Access Denied"))
        {
            System.out.println("Test 2 Passed login");
        } else {
            System.out.println("Test 2 Failed login");
        }

        //Thread.sleep(2000);
        userName.clear();
        //Thread.sleep(2000);
        passWord.clear();
        //Thread.sleep(2000);
        forgetPassWord.click();
        if (text.getText().equals("Forgot your password? Oops! we cant give it back to you... yet! :P"))
        {
            System.out.println("Test 3 Passed login");
        } else {
            System.out.println("Test 3 Failed login");
        }

        Thread.sleep(5000);

        driver.get("file:///Users/a11/Desktop/HTMLs/SignUp.html");
        WebElement sign_up_first_name = driver.findElement(By.id("first-name"));
        WebElement sign_up_last_name = driver.findElement(By.id("last-name"));
        WebElement sign_up_email = driver.findElement(By.id("email"));
        WebElement sign_up_password = driver.findElement(By.id("password"));
        WebElement sign_up_cpassword = driver.findElement(By.id("cpassword"));
        WebElement sign_up_test_check = driver.findElement(By.id("test-check"));
        WebElement sign_up_done = driver.findElement(By.id("done"));
        WebElement sign_up_cancel = driver.findElement(By.id("cancel"));

        sign_up_done.click();
        if (sign_up_test_check.getText().equals("Please Fill Name Field"))
        {
            System.out.println("Test 1 Passed sign_up");
        } else {
            System.out.println("Test 1 Failed sign_up");
        }

        //Thread.sleep(2000);
        sign_up_first_name.sendKeys("Alireza");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Please Fill last name Field"))
        {
            System.out.println("Test 2 Passed sign_up");
        } else {
            System.out.println("Test 2 Failed sign_up");
        }

        //Thread.sleep(2000);
        sign_up_last_name.sendKeys("Arjmand");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Please Enter Email"))
        {
            System.out.println("Test 3 Passed sign_up");
        } else {
            System.out.println("Test 3 Failed sign_up");
        }

        //Thread.sleep(2000);
        sign_up_email.sendKeys("Allarious@kapo.com");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Please Enter password"))
        {
            System.out.println("Test 4 Passed sign_up");
        } else {
            System.out.println("Test 4 Failed sign_up");
        }

        //Thread.sleep(2000);
        sign_up_password.sendKeys("12345");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Confirm Password"))
        {
            System.out.println("Test 5 Passed sign_up");
        } else {
            System.out.println("Test 5 Failed sign_up");
        }

        sign_up_cpassword.sendKeys("123");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Passwords Don't match"))
        {
            System.out.println("Test 6 Passed sign_up");
        } else {
            System.out.println("Test 6 Failed sign_up");
        }

        sign_up_cpassword.clear();
        sign_up_cpassword.sendKeys("12345");
        sign_up_done.click();
        //Thread.sleep(2000);
        if (sign_up_test_check.getText().equals("Welcome"))
        {
            System.out.println("Test 7 Passed sign_up");
        } else {
            System.out.println("Test 7 Failed sign_up");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/messages.html");
        WebElement messages_message = driver.findElement(By.id("message1"));
        WebElement messages_test_check = driver.findElement(By.id("test-check"));

        messages_message.click();
        if(messages_test_check.getText().equals("go to messages page"))
        {
            System.out.println("Test 1 Passed messages");
        }else {
            System.out.println("Test 1 Failed messages");
        }


        driver.get("file:///Users/a11/Desktop/HTMLs/ForgetPassword.html");
        WebElement forget_password_email = driver.findElement(By.id("email"));
        WebElement forget_password_done = driver.findElement(By.id("done"));
        WebElement forget_password_cancel = driver.findElement(By.id("cancel"));
        WebElement forget_password_test_check = driver.findElement(By.id("test-check"));

        forget_password_done.click();
        if(forget_password_test_check.getText().equals("go to please enter your email"))
        {
            System.out.println("Test 1 Passed ForgetPassword");
        }else {
            System.out.println("Test 1 Failed ForgetPassword");
        }
        forget_password_email.sendKeys("Allarious@Kapo.ir");
        forget_password_done.click();
        if(forget_password_test_check.getText().equals("go to the next page"))
        {
            System.out.println("Test 2 Passed ForgetPassword");
        }else {
            System.out.println("Test 2 Failed ForgetPassword");
        }
        forget_password_email.clear();

        driver.get("file:///Users/a11/Desktop/HTMLs/Footer.html");
        WebElement footer_email = driver.findElement(By.id("subscription"));
        WebElement footer_submit = driver.findElement(By.id("submit"));
        WebElement footer_test_check = driver.findElement(By.id("test-check"));

        footer_submit.click();
        if(footer_test_check.getText().equals("please enter your email"))
        {
            System.out.println("Test 1 Passed Footer");
        }else {
            System.out.println("Test 1 Failed Footer");
        }
        footer_email.sendKeys("Allarious@Kapo.ir");
        footer_submit.click();
        if(footer_test_check.getText().equals("go to the next page"))
        {
            System.out.println("Test 2 Passed Footer");
        }else {
            System.out.println("Test 2 Failed Footer");
        }
        footer_email.clear();

        driver.get("file:///Users/a11/Desktop/HTMLs/ChangePassword.html");
        WebElement change_password_old_password = driver.findElement(By.id("old-password"));
        WebElement change_password_new_password = driver.findElement(By.id("new-password"));
        WebElement change_password_verify_new_password = driver.findElement(By.id("verify-new-password"));
        WebElement change_password_submit = driver.findElement(By.id("submit"));
        WebElement change_password_cancel = driver.findElement(By.id("cancel"));
        WebElement change_password_test_check = driver.findElement(By.id("test-check"));

        change_password_submit.click();
        if(change_password_test_check.getText().equals("please enter your old password"))
        {
            System.out.println("Test 1 Passed ChangePassword");
        }else {
            System.out.println("Test 1 Failed ChangePassword");
        }
        change_password_old_password.sendKeys("12345");
        change_password_submit.click();
        if(change_password_test_check.getText().equals("please enter a new password"))
        {
            System.out.println("Test 2 Passed ChangePassword");
        }else {
            System.out.println("Test 2 Failed ChangePassword");
        }
        change_password_new_password.sendKeys("123");
        change_password_submit.click();
        if(change_password_test_check.getText().equals("please verify your new password"))
        {
            System.out.println("Test 3 Passed ChangePassword");
        }else {
            System.out.println("Test 3 Failed ChangePassword");
        }
        change_password_verify_new_password.sendKeys("1234");
        if(change_password_test_check.getText().equals("passwords dont match"))
        {
            System.out.println("Test 4 Passed ChangePassword");
        }else {
            System.out.println("Test 4 Failed ChangePassword");
        }
        change_password_verify_new_password.clear();
        change_password_verify_new_password.sendKeys("123");
        if(change_password_test_check.getText().equals("Done!"))
        {
            System.out.println("Test 5 Passed ChangePassword");
        }else {
            System.out.println("Test 5 Failed ChangePassword");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/Order.html");
        WebElement order_order = driver.findElement(By.id("order"));
        WebElement order_submit = driver.findElement(By.id("submit"));
        WebElement order_test_check = driver.findElement(By.id("test-check"));

        order_submit.click();
        if(order_test_check.getText().equals("please enter the order"))
        {
            System.out.println("Test 1 Passed Order");
        }else {
            System.out.println("Test 1 Failed Order");
        }
        order_order.sendKeys("gif me a Tofel right now!");
        order_submit.click();
        if(order_test_check.getText().equals("go next!"))
        {
            System.out.println("Test 2 Passed Order");
        }else {
            System.out.println("Test 2 Failed Order");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/Wallet_management/Dollar_management.html");
        WebElement dollar_management_submit = driver.findElement(By.id("submit"));
        WebElement dollar_management_test_check = driver.findElement(By.id("submit"));

        dollar_management_submit.click();
        if(dollar_management_test_check.getText().equals("please fill at least one of the fields"))
        {
            System.out.println("Test 1 Passed Dollar_management");
        }else {
            System.out.println("Test 1 Failed Dollar_management");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/Wallet_management/Euro_management.html");
        WebElement Euro_management_submit = driver.findElement(By.id("submit"));
        WebElement Euro_management_test_check = driver.findElement(By.id("submit"));

        Euro_management_submit.click();
        if(Euro_management_test_check.getText().equals("please fill at least one of the fields"))
        {
            System.out.println("Test 1 Passed Euro_management");
        }else {
            System.out.println("Test 1 Failed Euro_management");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/Wallet_management/Rial_management.html");
        WebElement Rial_management_submit = driver.findElement(By.id("submit"));
        WebElement Rial_management_test_check = driver.findElement(By.id("submit"));

        Rial_management_submit.click();
        if(Rial_management_test_check.getText().equals("please fill at least one of the fields"))
        {
            System.out.println("Test 1 Passed Rial_management");
        }else {
            System.out.println("Test 1 Failed Rial_management");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/User_Management/User_management_profile.html");
        WebElement user_management_profile_name = driver.findElement(By.id("name"));
        WebElement user_management_profile_lastname = driver.findElement(By.id("lastname"));
        WebElement user_management_profile_email = driver.findElement(By.id("email"));
        WebElement user_management_profile_phone_no = driver.findElement(By.id("phone-no"));
        WebElement user_management_profile_number = driver.findElement(By.id("number"));
        WebElement user_management_profile_rial_wallet = driver.findElement(By.id("rial-wallet"));
        WebElement user_management_profile_euro_wallet = driver.findElement(By.id("euro-wallet"));
        WebElement user_management_profile_dollar_wallet = driver.findElement(By.id("dollar-wallet"));
        WebElement user_management_profile_change_password = driver.findElement(By.id("change-password"));
        WebElement user_management_profile_change_profile_info = driver.findElement(By.id("change-profile-info"));
        WebElement user_management_profile_test_check = driver.findElement(By.id("test-check"));

        user_management_profile_change_password.click();
        if(user_management_profile_test_check.getText().equals("go to change password page"))
        {
            System.out.println("Test 1 Passed User_management_profile");
        }else {
            System.out.println("Test 1 Failed User_management_profile");
        }

        user_management_profile_name.sendKeys("Alireza");
        user_management_profile_lastname.sendKeys("Arjmand");
        user_management_profile_email.sendKeys("Allarious@Kapo.ir");
        user_management_profile_phone_no.sendKeys("09111111111");
        user_management_profile_number.sendKeys("0210000000");
        user_management_profile_change_profile_info.click();
        if (user_management_profile_test_check.equals("info changed"))
        {
            System.out.println("Test 2 Passed User_management_profile");
        }else {
            System.out.println("Test 2 Failed User_management_profile");
        }


        driver.get("file:///Users/a11/Desktop/HTMLs/User/User_Management/User_management_rial_payments.html");
        WebElement user_management_rial_payments_more_info = driver.findElement(By.id("more-info"));
        WebElement user_management_rial_payments_test_check = driver.findElement(By.id("test-check"));

        user_management_rial_payments_more_info.click();
        if(user_management_rial_payments_test_check.getText().equals("go to receipt"))
        {
            System.out.println("Test 1 Passed User_management_rial_payments");
        }else {
            System.out.println("Test 1 Failed User_management_rial_payments");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/User/User_Management/User_management_transactions.html");
        WebElement user_management_transactions_more_info = driver.findElement(By.id("more-info"));
        WebElement user_management_transactions_test_check = driver.findElement(By.id("test-check"));

        user_management_transactions_more_info.click();
        if(user_management_transactions_test_check.getText().equals("go to receipt"))
        {
            System.out.println("Test 1 Passed User_management_rial_payments");
        }else {
            System.out.println("Test 1 Failed User_management_rial_payments");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/Employee/Order_table.html");
        WebElement order_table_profile = driver.findElement(By.id("profile"));
        WebElement order_table_receipt = driver.findElement(By.id("receipt"));
        WebElement order_table_report = driver.findElement(By.id("report"));
        WebElement order_table_validate = driver.findElement(By.id("validate"));
        WebElement order_table_test_check = driver.findElement(By.id("test-check"));

        order_table_profile.click();
        if(order_table_test_check.getText().equals("go to profile"))
        {
            System.out.println("Test 1 Passed Order_table");
        }else {
            System.out.println("Test 1 Failed Order_table");
        }

        order_table_receipt.click();
        if(order_table_test_check.getText().equals("go to receipt"))
        {
            System.out.println("Test 2 Passed Order_table");
        }else {
            System.out.println("Test 2 Failed Order_table");
        }

        order_table_report.click();
        if(order_table_test_check.getText().equals("go to report"))
        {
            System.out.println("Test 3 Passed Order_table");
        }else {
            System.out.println("Test 3 Failed Order_table");
        }

        order_table_validate.click();
        if(order_table_test_check.getText().equals("go to validate"))
        {
            System.out.println("Test 4 Passed Order_table");
        }else {
            System.out.println("Test 4 Failed Order_table");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/Employee/Old_order_table.html");
        WebElement old_order_table_profile = driver.findElement(By.id("profile"));
        WebElement old_order_table_receipt = driver.findElement(By.id("receipt"));
        WebElement old_order_table_report = driver.findElement(By.id("report"));
        WebElement old_order_table_test_check = driver.findElement(By.id("test-check"));

        old_order_table_profile.click();
        if(old_order_table_test_check.getText().equals("go to profile"))
        {
            System.out.println("Test 1 Passed Old_order_table");
        }else {
            System.out.println("Test 1 Failed Old_order_table");
        }

        old_order_table_receipt.click();
        if(old_order_table_test_check.getText().equals("go to receipt"))
        {
            System.out.println("Test 2 Passed Old_order_table");
        }else {
            System.out.println("Test 2 Failed Old_order_table");
        }

        old_order_table_report.click();
        if(old_order_table_test_check.getText().equals("go to report"))
        {
            System.out.println("Test 3 Passed Old_order_table");
        }else {
            System.out.println("Test 3 Failed Old_order_table");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/Manager/Add_User.html");
        WebElement add_user_id = driver.findElement(By.id("id"));
        WebElement add_user_username = driver.findElement(By.id("username"));
        WebElement add_user_email = driver.findElement(By.id("email"));
        WebElement add_user_password = driver.findElement(By.id("password"));
        WebElement add_user_confirm_password = driver.findElement(By.id("confirm-password"));
        WebElement add_user_submit = driver.findElement(By.id("submit"));
        WebElement add_user_cancel = driver.findElement(By.id("cancel"));
        WebElement add_user_test_check = driver.findElement(By.id("test-check"));

        add_user_submit.click();
        if(add_user_test_check.getText().equals("please enter id"))
        {
            System.out.println("Test 1 Passed Add_User");
        }else {
            System.out.println("Test 1 Failed Add_User");
        }
        add_user_id.sendKeys("123125");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("please enter username"))
        {
            System.out.println("Test 2 Passed Add_User");
        }else {
            System.out.println("Test 2 Failed Add_User");
        }
        add_user_username.sendKeys("Allarious");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("please enter email"))
        {
            System.out.println("Test 3 Passed Add_User");
        }else {
            System.out.println("Test 3 Failed Add_User");
        }
        add_user_email.sendKeys("Allarious@Kapo.ir");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("please enter password"))
        {
            System.out.println("Test 4 Passed Add_User");
        }else {
            System.out.println("Test 4 Failed Add_User");
        }
        add_user_password.sendKeys("1212323");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("please confirm password"))
        {
            System.out.println("Test 5 Passed Add_User");
        }else {
            System.out.println("Test 5 Failed Add_User");
        }
        add_user_confirm_password.sendKeys("12123");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("passwords don't match"))
        {
            System.out.println("Test 6 Passed Add_User");
        }else {
            System.out.println("Test 6 Failed Add_User");
        }
        add_user_confirm_password.clear();
        add_user_confirm_password.sendKeys("1212323");
        add_user_submit.click();
        if(add_user_test_check.getText().equals("User added"))
        {
            System.out.println("Test 7 Passed Add_User");
        }else {
            System.out.println("Test 7 Failed Add_User");
        }

        driver.get("file:///Users/a11/Desktop/HTMLs/Manager/Add_employee.html");
        WebElement add_employee_id = driver.findElement(By.id("id"));
        WebElement add_employee_username = driver.findElement(By.id("username"));
        WebElement add_employee_email = driver.findElement(By.id("email"));
        WebElement add_employee_password = driver.findElement(By.id("password"));
        WebElement add_employee_confirm_password = driver.findElement(By.id("confirm-password"));
        WebElement add_employee_salary = driver.findElement(By.id("salary"));
        WebElement add_employee_submit = driver.findElement(By.id("submit"));
        WebElement add_employee_cancel = driver.findElement(By.id("cancel"));
        WebElement add_employee_test_check = driver.findElement(By.id("test-check"));

        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("please enter id"))
        {
            System.out.println("Test 1 Passed add_employee");
        }else {
            System.out.println("Test 1 Failed add_employee");
        }
        add_employee_id.sendKeys("123125");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("please enter username"))
        {
            System.out.println("Test 2 Passed add_employee");
        }else {
            System.out.println("Test 2 Failed add_employee");
        }
        add_employee_username.sendKeys("Allarious");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("please enter email"))
        {
            System.out.println("Test 3 Passed add_employee");
        }else {
            System.out.println("Test 3 Failed add_employee");
        }
        add_employee_email.sendKeys("Allarious@Kapo.ir");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("please enter password"))
        {
            System.out.println("Test 4 Passed add_employee");
        }else {
            System.out.println("Test 4 Failed add_employee");
        }
        add_employee_password.sendKeys("1212323");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("please confirm password"))
        {
            System.out.println("Test 5 Passed add_employee");
        }else {
            System.out.println("Test 5 Failed add_employee");
        }
        add_employee_confirm_password.sendKeys("12123");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("passwords don't match"))
        {
            System.out.println("Test 6 Passed add_employee");
        }else {
            System.out.println("Test 6 Failed add_employee");
        }
        add_employee_confirm_password.clear();
        add_employee_confirm_password.sendKeys("1212323");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("User added"))
        {
            System.out.println("Test 7 Passed add_employee");
        }else {
            System.out.println("Test 7 Failed add_employee");
        }
        add_employee_salary.sendKeys("1000000 Rial");
        add_employee_submit.click();
        if(add_employee_test_check.getText().equals("User added"))
        {
            System.out.println("Test 8 Passed add_employee");
        }else {
            System.out.println("Test 8 Failed add_employee");
        }



        driver.get("file:///Users/a11/Desktop/HTMLs/Manager/Employee_table.html");
        WebElement employee_table_add = driver.findElement(By.id("add"));
        WebElement employee_table_profile = driver.findElement(By.id("profile"));
        WebElement employee_table_ban = driver.findElement(By.id("ban"));
        WebElement employee_table_message = driver.findElement(By.id("message"));
        WebElement employee_table_salary = driver.findElement(By.id("salary"));
        WebElement employee_table_delete = driver.findElement(By.id("delete"));
        WebElement employee_table_test_check = driver.findElement(By.id("test-check"));

        employee_table_add.click();
        if(employee_table_test_check.getText().equals("go to add employee page"))
        {
            System.out.println("Test 1 Passed employee_table");
        }else {
            System.out.println("Test 1 Failed employee_table");
        }

        employee_table_profile.click();
        if(employee_table_test_check.getText().equals("go to profile page"))
        {
            System.out.println("Test 2 Passed employee_table");
        }else {
            System.out.println("Test 2 Failed employee_table");
        }

        employee_table_ban.click();
        if(employee_table_test_check.getText().equals("go to ban page"))
        {
            System.out.println("Test 3 Passed employee_table");
        }else {
            System.out.println("Test 3 Failed employee_table");
        }

        employee_table_message.click();
        if(employee_table_test_check.getText().equals("go to message page"))
        {
            System.out.println("Test 4 Passed employee_table");
        }else {
            System.out.println("Test 4 Failed employee_table");
        }

        employee_table_salary.click();
        if(employee_table_test_check.getText().equals("go to salary page"))
        {
            System.out.println("Test 5 Passed employee_table");
        }else {
            System.out.println("Test 5 Failed employee_table");
        }

        employee_table_delete.click();
        if(employee_table_test_check.getText().equals("delete employee"))
        {
            System.out.println("Test 6 Passed employee_table");
        }else {
            System.out.println("Test 6 Failed employee_table");
        }


        driver.get("file:///Users/a11/Desktop/HTMLs/Manager/User_table.html");
        WebElement user_table_add = driver.findElement(By.id("add"));
        WebElement user_table_profile = driver.findElement(By.id("profile"));
        WebElement user_table_ban = driver.findElement(By.id("ban"));
        WebElement user_table_message = driver.findElement(By.id("message"));
        WebElement user_table_delete = driver.findElement(By.id("delete"));
        WebElement user_table_test_check = driver.findElement(By.id("test-check"));

        user_table_add.click();
        if(user_table_test_check.getText().equals("go to add employee page"))
        {
            System.out.println("Test 1 Passed user_table");
        }else {
            System.out.println("Test 1 Failed user_table");
        }

        user_table_profile.click();
        if(user_table_test_check.getText().equals("go to profile page"))
        {
            System.out.println("Test 2 Passed user_table");
        }else {
            System.out.println("Test 2 Failed user_table");
        }

        user_table_ban.click();
        if(user_table_test_check.getText().equals("go to ban page"))
        {
            System.out.println("Test 3 Passed user_table");
        }else {
            System.out.println("Test 3 Failed user_table");
        }

        user_table_message.click();
        if(user_table_test_check.getText().equals("go to message page"))
        {
            System.out.println("Test 4 Passed user_table");
        }else {
            System.out.println("Test 4 Failed user_table");
        }

        user_table_delete.click();
        if(user_table_test_check.getText().equals("delete employee"))
        {
            System.out.println("Test 5 Passed user_table");
        }else {
            System.out.println("Test 5 Failed user_table");
        }

        driver.quit();
    }
}



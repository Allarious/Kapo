import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.io.File;

public class Main {

        public static void main(String[] args) throws InterruptedException {
            //beta 2 version
//            File gecko = new File("./Desktop/geckodriver");
            File gecko = new File("/Users/a11/Desktop/newHTMLS/geckodriver");
            System.setProperty("webdriver.gecko.driver", gecko.getAbsolutePath());
            //beta 1 version
//            System.setProperty("webdriver.gecko.driver", "./geckodriver.exe");

        WebDriver driver = new FirefoxDriver();
            driver.get("file:///Users/a11/Desktop/Phase%203/LoginPage/index.html");
            WebElement text = driver.findElement(By.id("welcome"));
            WebElement userName = driver.findElement(By.id("login_username"));
            WebElement passWord = driver.findElement(By.id("login_password"));
            WebElement loginButton = driver.findElement(By.id("login_button"));
            WebElement forgetPassWord = driver.findElement(By.id("forget-label"));

            Thread.sleep(2000);
            userName.sendKeys("Allarious");
            Thread.sleep(2000);
            passWord.sendKeys("12345");
            Thread.sleep(2000);
            loginButton.click();
            if (text.getText().equals("Access Granted"))
            {
                System.out.println("Test 1 Passed");
            } else {
                System.out.println("Test 1 failed");
            }

            Thread.sleep(2000);
            userName.clear();
            userName.sendKeys("NotAUser");
            Thread.sleep(2000);
            passWord.clear();
            passWord.sendKeys("12333");
            Thread.sleep(2000);
            loginButton.click();
            if (text.getText().equals("Access Denied"))
            {
                System.out.println("Test 2 Passed");
            } else {
                System.out.println("Test 2 failed");
            }

            Thread.sleep(2000);
            userName.clear();
            Thread.sleep(2000);
            passWord.clear();
            Thread.sleep(2000);
            forgetPassWord.click();
            if (text.getText().equals("Forgot your password? Oops! we cant give it back to you... yet! :P"))
            {
                System.out.println("Test 3 Passed");
            } else {
                System.out.println("Test 3 failed");
            }

                    Thread.sleep(5000);
                    driver.quit();
        }
    }



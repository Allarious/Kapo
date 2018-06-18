import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;

import java.io.File;

public class main {

    public static void main(String[] args) throws InterruptedException {

        File gecko = new File("/Users/a11/Desktop/newHTMLS/geckodriver");
        System.setProperty("webdriver.gecko.driver", gecko.getAbsolutePath());

        WebDriver driver = new FirefoxDriver();
        driver.get("/Users/a11/Desktop/newHTMLS/ContactUs/index.html");

        WebElement text = driver.findElement(By.id("contact-text"));
        WebElement userName = driver.findElement(By.id("username"));
        WebElement email = driver.findElement(By.id("email"));
        WebElement phone = driver.findElement(By.id("phone"));
        WebElement webSite = driver.findElement(By.id("website"));
        WebElement message = driver.findElement(By.id("message"));
        WebElement submitButton = driver.findElement(By.id("contact-submit"));

        Thread.sleep(2000);
        submitButton.click();
        if (text.getText().equals("Please Fill Name Field"))
        {
            System.out.println("Test 1 Passed");
        } else {
            System.out.println("Test 1 failed");
        }

        Thread.sleep(2000);
        userName.sendKeys("Allarious");
        submitButton.click();
        Thread.sleep(2000);
        if (text.getText().equals("Please Fill Email Field"))
        {
            System.out.println("Test 2 Passed");
        } else {
            System.out.println("Test 2 failed");
        }

        Thread.sleep(2000);
        email.sendKeys("NotInEmailFormat");
        submitButton.click();
        Thread.sleep(2000);
        if (text.getText().equals("Please Enter Email Correctly"))
        {
            System.out.println("Test 3 Passed");
        } else {
            System.out.println("Test 3 failed");
        }

        Thread.sleep(2000);
        email.clear();
        email.sendKeys("Allarious@kapo.com");
        submitButton.click();
        Thread.sleep(2000);
        if (text.getText().equals("Please Enter Text"))
        {
            System.out.println("Test 4 Passed");
        } else {
            System.out.println("Test 4 failed");
        }

        Thread.sleep(2000);
        message.sendKeys("I wish you a really good day :)");
        submitButton.click();
        Thread.sleep(2000);
        if (text.getText().equals("Contact Form"))
        {
            System.out.println("Test 5 Passed");
        } else {
            System.out.println("Test 5 failed");
        }

        Thread.sleep(5000);
        driver.quit();
    }
}



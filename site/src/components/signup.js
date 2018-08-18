import React from 'react';
import classes from './Authentication/signup.css';
import Inp from './Authentication/input';
import Button from './Authentication/button';

const SignUpPage = () => {
    return (
        <div className={classes["signup-container"]}>
            <div className={classes.logo}></div>
            <Inp holder="First Name" type="text"/>
            <Inp holder="Last Name" type="text"/>
            <Inp holder="Username" type="text"/>
            <Inp holder="E-mail" type="email"/>
            <Inp holder="Password" type="password"/>
            <Inp holder="Confirm Password" type="password"/>
            <Button>Sign Up</Button>
            <p className={classes["conditions-of-use"]}>By signing up you agree to our <a href="">Conditions of use</a></p>
        </div>
    );
};

export default SignUpPage;
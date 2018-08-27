import React from 'react';
import classes from './authentication/signup.css';
import Inp from './inputs/input';
import Authbutton from './buttons/authbutton';

const SignUpPage = (props) => {
    return (
        <div className={classes["signup-container"]}>
            <div className={classes.logo}></div>
            <Inp holder="First Name" type="text"/>
            <Inp holder="Last Name" type="text"/>
            <Inp holder="Username" type="text"/>
            <Inp holder="E-mail" type="email"/>
            <Inp holder="Password" type="password"/>
            <Inp holder="Confirm Password" type="password"/>
            <select className={classes.gender}>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
                <option value="None">None</option>
                <option value="Prefer Not To Say">Prefer Not To Say</option>
            </select>
            <Authbutton>Sign Up</Authbutton>
            <p className={classes["conditions-of-use"]}>By signing up you agree to our <a className={classes["conditions-of-use-a"]} onClick={() => props.clicked('ConditionsofUse')}>Conditions of use</a></p>
        </div>
    );
};

export default SignUpPage;
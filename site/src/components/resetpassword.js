import React from 'react';
import classes from './Authentication/resetpassword.css';
import Inp from './Authentication/input';
import Button from './Authentication/button';

const ResetPassword = () => {
    return (
        <div className={classes["reset-password-container"]}>
            <div className={classes.logo}></div>
            <Inp holder="Enter Your Email" type="text"/>
            <Button>Confirm</Button>
        </div>
    );
};

export default ResetPassword;
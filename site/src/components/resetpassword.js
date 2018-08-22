import React from 'react';
import classes from './authentication/resetpassword.css';
import Inp from './inputs/input';
import Authbutton from './buttons/authbutton';

const ResetPassword = () => {
    return (
        <div className={classes["reset-password-container"]}>
            <div className={classes.logo}></div>
            <Inp holder="Enter Your Email" type="text"/>
            <Authbutton>Confirm</Authbutton>
        </div>
    );
};

export default ResetPassword;
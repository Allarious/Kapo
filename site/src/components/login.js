import React from 'react';
import classes from './Authentication/login.css';
import Inp from './inputs/input';
import Authbutton from './Buttons/authbutton';

const LoginPage = (props) => {
  return (
      <div className={classes["login-container"]}>
          <div className={classes.logo}></div>
          <Inp holder="Username" type="text"/>
          <Inp holder="Password" type="password"/>
          <Authbutton>Login</Authbutton>
          <p className={classes["forget-password"]} onClick={() => props.clicked('ForgetPassword')}>Forgot Your Password?</p>
      </div>
  );
};

export default LoginPage;
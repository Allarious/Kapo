import React from 'react';
import classes from './Authentication/login.css';
import Inp from './Authentication/input';
import Button from './Authentication/button';

const LoginPage = (props) => {
  return (
      <div className={classes["login-container"]}>
          <div className={classes.logo}></div>
          <Inp holder="Username" type="text"/>
          <Inp holder="Password" type="password"/>
          <Button>Login</Button>
          <p className={classes["forget-password"]} onClick={() => props.clicked('ForgetPassword')}>Forgot Your Password?</p>
      </div>
  );
};

export default LoginPage;
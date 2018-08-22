import React from 'react';
import classes from './input.css';

const Input = (props) => {
    return (
      <div>
          <input className={classes["login-input"]} type={props.type} placeholder={props.holder}/>
      </div>
    );
};

export default Input;
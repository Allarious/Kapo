import React from 'react';

import classes from './button.css';

const Button = (props) => {
    return <button className={classes["form-button"]}>{props.children}</button>;
};

export default Button;
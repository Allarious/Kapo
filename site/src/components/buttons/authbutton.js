import React from 'react';

import classes from './authbutton.css';

const Authbutton = (props) => {
    return <button className={classes["form-button"]}>{props.children}</button>;
};

export default Authbutton;
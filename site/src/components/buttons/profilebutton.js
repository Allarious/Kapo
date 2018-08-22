import React from 'react';

import classes from './profilebutton.css';

const Profilebutton = (props) => {
    return <button className={classes["form-button"]}>{props.children}</button>;
};

export default Profilebutton;
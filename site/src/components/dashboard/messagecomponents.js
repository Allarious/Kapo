import React from 'react';

import classes from './messagecomponents.css';

export const Messagecomponents = (props) => {

    return(
        <div className={classes.container}>
            <div className={classes.from}>{props.from}</div>
            <div className={classes.name}>{props.name}</div>
            <div className={classes.thumbnail}>{props.thumbnail}</div>
            <div className={classes.condition}>{props.condition}</div>
            <div className={classes.break}></div>
            <div className={classes.message}>{props.message}</div>
        </div>
    );
};

export default Messagecomponents;
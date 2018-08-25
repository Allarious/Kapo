import React from 'react';

import classes from './notification.css';

const Notification = (props) => {
    return(<div className={classes.container}>

        <div className={classes.header}>{props.header}</div>
        <div className={classes.condition}>{props.condition}</div>

    </div>);
};

export default Notification;
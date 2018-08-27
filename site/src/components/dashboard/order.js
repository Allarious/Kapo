import React from 'react';

import classes from './order.css';

const Order = (props) => {
    let style = {
        color: 'lightgreen',
    };
    return(
        <div className={classes.container}>
            <div className={classes.left}><a>@{props.username}</a></div>
            <div className={classes.middle}>{props.type}</div>
            <div className={classes.middle}>{props.costR}</div>
            <div className={classes.middle}>{props.date}</div>
            <div className={classes.middle}>{props.time}</div>
            <div className={classes.right} style={style}>{props.condition}</div>
            <div className={classes.break}></div>
            <div className={classes["more-info"]}>{props.moreInfo}</div>
        </div>
    );
};

export default Order;
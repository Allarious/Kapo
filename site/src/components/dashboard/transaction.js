import React from 'react';

import classes from './transaction.css';

const Transaction = (props) => {
    return(
        <div className={classes.container}>
            <div className={classes.left}>{props.type}</div>
            <div className={classes.middle}>{props.costR}</div>
            <div className={classes.middle}>{props.costD}</div>
            <div className={classes.middle}>{props.date}</div>
            <div className={classes.middle}>{props.time}</div>
            <div className={classes.right}>{props.condition}</div>
            <div className={classes.break}></div>
            <div className={classes["more-info"]}>{props.moreInfo}</div>
        </div>
    );
};

export default Transaction;
import React from 'react';

import classes from './transaction.css';

const Transaction = (props) => {
    let style = {
        color: 'lightgreen',
    }
    return(
        <div className={classes.container}>
            <div className={classes.left}><a>@{props.username}</a></div>
            <div className={classes.middle}>{props.type}</div>
            <div className={classes.middle}>{props.costR}</div>
            <div className={classes.middle}>{props.date}</div>
            <div className={classes.middle}>{props.time}</div>
            {/*<div className={classes.right} style={style}>{props.condition}</div> */}
            <div className={classes.right}>

                <div className={classes["btn-container"]}>
                    <div className={classes.accept}></div>
                    <div className={classes.reject}></div>
                </div>

            </div>
            <div className={classes.break}></div>
            <div className={classes["more-info"]}>{props.moreInfo}</div>
        </div>
    );
};

export default Transaction;
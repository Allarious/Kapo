import React from 'react';

import classes from './card.css';

const Card = (props) => {

    let proPic = <div></div>

    if (props.ind === "0")
    {
        proPic = <div className={classes["pro-pic1"]}/>;
    }else if(props.ind === "1"){
        proPic = <div className={classes["pro-pic2"]}/>;
    }else if(props.ind === "2"){
        proPic = <div className={classes["pro-pic3"]}/>;
    }else {
        proPic = <div className={classes["pro-pic3"]}/>;
    }
    return(<div className={classes.container}>
        {proPic}
        <div className={classes.name}>{props.name}</div>
        <div className={classes.title}>{props.title}</div>
        <div className={classes.desc}>
            <div className={classes.town}> {props.town}</div>
            <div className={classes.country}>{props.country}</div>
            <div className={classes["button-container"]}>
                <div className={classes.github}></div>
                <div className={classes.twitter}></div>
                <div className={classes.facebook}></div>
            </div>
        </div>
    </div>);
};

export default Card;
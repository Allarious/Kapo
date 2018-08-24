import React from 'react';

import classes from './acc.css';

const Acc = (props) => {

    let divStyle ={
      backgroundImage: 'url(' + props.image + ')',
    };

    return (<div className={classes.container}>
        <div className={classes.im} style={divStyle}></div>
        <div className={classes["pro-image"]} style={divStyle}></div>
        <div className={classes.name}>{props.name}</div>
        <div className={classes.role}>{props.role}</div>
    </div>);
};

export default Acc;
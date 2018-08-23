import React from 'react';

import classes from './converttype.css';
import Button from './../buttons/authbutton';
import Inp from './../inputs/input';

const ConvertType = (props) => {

    let image = <div></div>
    let charge = "";
    let explain = "";
    let converter = <div></div>

    if (props.index === 0) {
        image = <div className={classes.logo}></div>
        charge = "Charge";
        explain = "Charge your wallet";
        converter = (<div>
            <Inp type="text" holder="Amount to charge (R)"/>
        </div>)
    } else if (props.index === 1){
        image = <div className={classes.logo1}></div>
        charge = "Change";
        explain = "Change from Rial to Dollar";
        converter = (<div>
            <Inp type="text" holder="Amount to change (R)"/>
            <div className={classes.to}>To :</div>
            <Inp type="text" holder="Amount to charge ($)"/>
        </div>)
    } else if (props.index === 2){
        image = <div className={classes.logo2}></div>
        charge = "Change";
        explain = "Change from Rial to Euro";
        converter = (<div>
            <Inp type="text" holder="Amount to change (R)"/>
            <div className={classes.to}>To :</div>
            <Inp type="text" holder="Amount to charge (E)"/>
        </div>)
    }
    return (<div className={classes.content}>
        {image}
        <div className={classes.remain}>
            Remains : {props.remain}
        </div>
        <div className={classes.explain}>
            {explain}
        </div>
        {converter}
        <Button>{charge}</Button>
        </div>);

};

export default ConvertType;
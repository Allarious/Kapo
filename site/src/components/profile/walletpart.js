import React from 'react';

import classes from './walletpart.css';

const WalletPart = (props) => {
    return(
        <div className={classes.container} onClick={() => props.clicked("Convert")}>
            <div className={classes.name}>{props.moneyType} :&nbsp;</div>
            <div className={classes.amount}>{props.amount}</div>
        </div>
    );
};

export default WalletPart;
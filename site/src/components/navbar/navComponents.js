import React from 'react';

import classes from './navbar.css';

const NavComponents = (props) => {

    let pop = props.pop;

    let content = <div></div>

    if (props.pop != undefined)
    {
        content = <div className={classes.pop}>{pop}</div>
    }

    return (
        <div className={classes.navComponents} onClick={props.clicked}>
            {props.children}
            {content}
        </div>);
};

export default NavComponents;
import React from 'react';

import classes from './navbar.css';

const NavComponents = (props) => {
  return (<div className={classes.navComponents} onClick={props.clicked}> {props.children} </div>);
};

export default NavComponents;
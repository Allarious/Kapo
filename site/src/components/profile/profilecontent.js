import React from 'react';

import classes from './profilecontent.css';


const ProfileContent = (props) => {
    return(<div className={classes.container}>
        <div className={classes.name}>{props.attname} : &nbsp;</div>
        <div className={classes.cont}>{props.attcont}</div>
    </div>);
};

export default ProfileContent;
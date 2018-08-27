import React from 'react';

import classes from './ourteam.css';
import Card from './card';


const OurTeam = () => {
    return (
        <div className={classes.container}>
            <Card name="Alireza Arjmand" title="shitty swimmer" ind="0" town="Tehran" country="Iran"/>
            <Card name="Amin Isaai" title="expert hand to hand combatant" ind="1" town="Tehran" country="Iran"/>
            <Card name="Reza Bigdeli" title="Criminal master mind" ind="2" town="Zanjan" country="Iran"/>
        </div>
    );
};

export default OurTeam;
import React from 'react';
import classes from './navbar/navbar.css';

import NavComponents from './navbar/navComponents'


const Navbar = (props) => {

    let cpms = [
        {text :'HomePage',
            clicked: 'Homepage',
            id:'c1'},
        {text :'Profile',
            clicked: 'Profile',
            id:'c2'},
        {text :'Login',
            clicked: 'Login',
            id:'c3'},
        {text :'Signup',
            clicked:'Signup',
            id:'c4'},
        {text :'Logout',
            clicked:'Homepage',
            id:'c5'},
    ];

    return(
        <div className={classes.navbar}>
            {cpms.map((obj) => {
                return <NavComponents key={obj.id} clicked={() => props.clicked(obj.clicked)}> {obj.text} </NavComponents>;
            })}
        </div>
    );

};

export default Navbar;
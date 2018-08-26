import React from 'react';

import classes from './accounts/accounts.css';
import Acc from './accounts/acc';
import Inp from './inputs/input';
import Button from './buttons/authbutton';

const Accounts = (props) => {

    let account = [
        {
            name: "Ursula Gurnmeister",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample1.jpg",
            role:"User",
            id:'a1',
        },
        {
            name: "Jason Response",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample7.jpg",
            role:"User",
            id:'a2',
        },
        {
            name: "Lily Pitt",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample6.jpg",
            role:"User",
            id:'a3',
        },
        {
            name: "Jane Doe",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample2.jpg",
            role:"User",
            id:'a4',
        },
        {
            name: "Samaneh Zarghami",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample3.jpg",
            role:"User",
            id:'a5',
        },
        {
            name: "George Jolie",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample4.jpg",
            role:"User",
            id:'a6',
        },
        {
            name: "Ehsan Ahmadi",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample5.jpg",
            role:"User",
            id:'a7',
        },
        {
            name: "Druid Wensleydale",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample8.jpg",
            role:"User",
            id:'a8',
        },
        {
            name: "Nazanin Babaei",
            image:"https://s3-us-west-2.amazonaws.com/s.cdpn.io/331810/profile-sample9.jpg",
            role:"User",
            id:'a9',
        },
    ];


    return(
        <div className={classes.container}>
            {account.map((event) => {
                return(<Acc key={event.id} image={event.image} role={event.role} name={event.name}/>);
            })}
            <div className={classes.add}>
                <div className={classes.circle}>
                    <div className={classes["ver-line"]}></div>
                    <div className={classes["hor-line"]}></div>
                </div>
                <div className={classes.modal}>
                    <Inp type="text" holder="Username"/>
                    <Inp type="text" holder="E-mail"/>
                    <Inp type="password" holder="Password"/>
                    <Button>Add</Button>
                </div>
            </div>
        </div>);
};

export default Accounts;
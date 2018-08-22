import React from 'react';

import classes from './profile/profile.css';

import Button from './buttons/profilebutton'
import Att from './profile/profilecontent';
import Table from './table/table';
import WalletPart from "./profile/walletpart";

const Profile = (props) => {

    const profile =[
        {att : 'First Name',
        attCont: 'Alireza',
        id: 'a1'},
        {att : 'Last Name',
            attCont: 'Arjmand',
            id: 'a2'},
        {att : 'E-mail',
            attCont: 'Alirezaicq4@gmail.com',
            id: 'a3'},
        {att : 'Contact Number',
            attCont: '09121234567',
            id: 'a4'},
        {att : 'Role',
            attCont: 'User',
            id: 'a5'},
        {att : 'Birth Date',
            attCont: '5/5/1950',
            id: 'a6'},
        {att : 'Joining Date',
            attCont: '7/5/1955',
            id: 'a7'},
    ];


    const wallet = [
        {
            money: "Rial",
            amount: "153000R",
            id:"m1"
        },
        {
            money:"Dollar",
            amount:"37$",
            id:"m2",
        },
        {
            money:"Euro",
            amount:"254E",
            id:"m3",
        },
    ];


    return(
        <div className={classes.container}>
            <div className={classes.title}>Profile Management</div>
            <div className={classes["profile-header"]}>
                <div className={classes["profile-pic"]}>
                </div>
            </div>
            <div className={classes.wallet}>
                {wallet.map((event) => {
                    return(
                        <WalletPart id={event.id} moneyType={event.money} amount={event.amount}/>
                    );
                })}
            </div>
            <div className={classes["profile-content"]}>
                    <div>
                        {profile.map((event) => {
                            return(
                                <Att id={event.id} attname={event.att} attcont={event.attCont}/>
                            );
                        })}
                    </div>
            </div>
            <div onClick={() => props.clicked('EditProfile')}>
            <Button>Edit Profile</Button>
            </div>
        </div>
    );
};

export default Profile;
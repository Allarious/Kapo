import React from 'react';
import classes from './profile/editprofile.css';
import Inp from './inputs/input';
import Button from './buttons/authbutton';

const EditProfile = () => {
    return (
        <div className={classes["signup-container"]}>
            <Inp holder="First Name" type="text"/>
            <Inp holder="Last Name" type="text"/>
            <Inp holder="Username" type="text"/>
            <Inp holder="E-mail" type="email"/>
            <Inp holder="Contact Number" type="text"/>
            <Button>Save Changes</Button>
        </div>
    );
};

export default EditProfile;
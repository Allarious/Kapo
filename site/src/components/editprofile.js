import React from 'react';
import classes from './profile/editprofile.css';
import Inp from './inputs/input';
import Button from './buttons/authbutton';

const EditProfile = () => {
    return (
        <div className={classes["signup-container"]}>
            <div className={classes["section-header"]}>Edit Profile</div>
            <Inp holder="First Name" type="text"/>
            <Inp holder="Last Name" type="text"/>
            <Inp holder="Username" type="text"/>
            <Inp holder="E-mail" type="email"/>
            <Inp holder="Contact Number" type="text"/>
            <Inp holder="Region" type="text"/>
            <Inp holder="Country" type="text"/>
            <Inp holder="Birth Date" type="text"/>
            <div className={classes.gap}></div>
            <div className={classes["section-header"]}>Change Password</div>
            <Inp holder="New Password" type="password"/>
            <Inp holder="Confirm New Password" type="password"/>
            <Inp holder="Old Password" type="password"/>
            <Button>Save Changes</Button>
        </div>
    );
};

export default EditProfile;
import React from 'react';

import classes from './sendmessage/sendmessage.css';
import Button from './buttons/profilebutton';

const SendMessage = () => {
    return(
        <div className={classes.container}>
            <div className={classes["send-to"]}>
                <div className={classes["send-to-container"]}>
                <div className={classes["send-to-image"]}>To:</div>
                <input className={classes["send-to-input"]}></input>
                </div>
            </div>
            <div className={classes.subject}>
                <div className={classes["subject-container"]}>
                <div className={classes["subject-image"]}>Subject:</div>
                <input className={classes["subject-input"]}></input>
                </div>
            </div>
            <div className={classes["text-body"]}>
                <textarea className={classes["text-body-input"]} type="text"/>
            </div>
            <Button>Send</Button>
        </div>
    );
};

export default SendMessage;
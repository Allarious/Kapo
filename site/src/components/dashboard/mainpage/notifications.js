import React from 'react';

import classes from './notifications.css';

import Notification from './notification';

const Notifications = () => {

    let notifications = [
        {
            header: "You Have A New message",
            condition: "New",
            id:"n1",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n2",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n3",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n4",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n5",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n6",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n7",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n8",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n9",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n10",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n11",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n12",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n13",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n14",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n15",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n16",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n17",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n18",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n19",
        },{
            header: "You Have A New message",
            condition: "New",
            id:"n20",
        },
    ];

    return(
        <div className={classes.container}>
            <div className={classes.header}>Notifications</div>
            {notifications.map((event) => {
                return(<Notification key={event.id} header={event.header} condition={event.condition}/>);
            })}
        </div>
    );

};

export default Notifications;
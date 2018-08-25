import React from 'react';

import classes from './orders.css';

import Order from './order';

const Orders = (props) => {

    let orders = [
        {
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't1',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't2',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't3',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't4',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't5',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't6',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't7',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't8',
        },{
            type: 'Tofel',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't9',
        },
    ];

    return(
        <div className={classes.container}>
            {orders.map((event) => {
                return (
                    <Order key={event.id}
                                 type={event.type}
                                 costR={event.costR}
                                 costD={event.costD}
                                 date={event.date}
                                 time={event.time}
                                 condition={event.condition}
                                 description={event.discription}/>
                );
            })}
        </div>
    );
};

export default Orders;
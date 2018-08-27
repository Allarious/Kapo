import React from 'react';

import classes from './transactions.css';

import Transaction from './transaction';

const Transactions = (props) => {

    let transactions = [
        {
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't1',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't2',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't3',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't4',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't5',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't6',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't7',
        },{
            username:'Someone',
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't8',
        },{
            username:'Someone',
            type: 'Rial',
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
            <div className={classes["auto-assign"]}>
                Auto Assign
            </div>
            {transactions.map((event) => {
                return (
                    <Transaction key={event.id}
                                      type={event.type}
                                      costR={event.costR}
                                      username={event.username}
                                      date={event.date}
                                      time={event.time}
                                      condition={event.condition}
                                        description={event.discription}/>
                );
            })}
        </div>
    );
};

export default Transactions;
import React from 'react';

import classes from './transactions.css';

import Transaction from './transaction';

const Transactions = (props) => {

    let transactions = [
        {
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't1',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't2',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't3',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't4',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't5',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't6',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't7',
        },{
            type: 'Rial',
            costR: '1530000',
            costD: '15',
            date: '3/3/1950',
            time: '22:37',
            condition: 'accepted',
            description:'cool bro',
            id: 't8',
        },{
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
            {transactions.map((event) => {
                return (
                    <Transaction key={event.id}
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

export default Transactions;
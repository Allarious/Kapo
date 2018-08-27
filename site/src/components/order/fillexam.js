import React from 'react';

import classes from './fillexam.css';

import Inp from './../inputs/input'
import Button from './../buttons/authbutton';
import PaymentMethod from './../paymentmethod';

const FillExam = (props) => {

    let inputs = [
        {
            holder: 'Full Name',
            id: 'i1',
        }, {
            holder: 'Card Number',
            id: 'i2',
        }, {
            holder: 'i.e. Tofel',
            id: 'i3',
        }, {
            holder: 'Country',
            id: 'i4',
        }, {
            holder: 'City',
            id: 'i5',
        }, {
            holder: 'Site Url',
            id: 'i6',
        }
    ];

    return (
        <div className={classes.container}>


            <div className={classes.header}>IELTS</div>
            <div className={classes.wage}>wage: 10$</div>

            {inputs.map((event) => {

                return (
                    <Inp key={event.id} holder={event.holder}/>
                );

            })}

            <PaymentMethod/>

            <div className={classes.txtareadiv}>
                <textarea className={classes.txtarea} placeholder="write your description here"></textarea>
            </div>

            <Button>Confirm</Button>

        </div>
    );

};

export default FillExam;